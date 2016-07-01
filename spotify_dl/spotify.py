from __future__ import unicode_literals
from spotify_dl.scaffold import *
from spotify_dl.tokens import *

import spotipy.util as util
import youtube_dl


def authenticate():
    """Authenticates you to Spotify
    """
    return util.prompt_for_user_token(username,scope, CLIENT_ID, CLIENT_SECRET, REDIRECT_URL)


def fetch_tracks(sp, playlist, user_id):
    """Fetches tracks from Spotify user's saved tracks or from playlist(if playlist parameter is passed
       and saves song name and artist name to songs list
    """
    log.debug('Fetching saved tracks')
    offset = 0
    songs = []
    if user_id is None:
        current_user_id = sp.current_user()['id']
    else:
        current_user_id = user_id
    while True:
        if playlist is None:
            results = sp.current_user_saved_tracks(limit=50, offset=offset)
        else:
            results = sp.user_playlist_tracks(current_user_id, playlist, None, limit=50, offset=offset)

        log.debug('Got result json {}'.format(results))
        for item in results['items']:
            track = item['track']
            log.debug('Appending {} to songs list'.format(track['name'] + ' - ' + track['artists'][0]['name']))
            songs.append(track['name'] + ' - ' + track['artists'][0]['name'])
            offset += 1

        if results.get('next') is None:
            log.info('All pages fetched, time to leave. Added {} songs in total'.format(offset))
            break
    return songs


def save_songs_to_file(songs):
    """
    :param songs
    Saves the songs fetched from fetch_tracks function to songs.txt file
       to be downloaded from youtube-dl
    """

    with open('songs.txt', 'w') as f:
        f.write('\n'.join(songs))
    f.close()


def download_songs(songs, download_directory):
    """
    Downloads songs from the YouTube URL passed to either
       current directory or download_directory, is it is passed
    """

    ydl_opts = {
        'format': 'bestaudio/best',
        'download_archive': 'downloaded_songs.txt',
        'outtmpl': download_directory+'%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    log.debug('Songs to download: {}'.format(songs))
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for item in songs:
            try:
                ydl.download([item])
            except Exception:
                print('Failed to download: {}'.format(item))
                continue

