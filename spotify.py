from __future__ import unicode_literals
from scaffold import *
from tokens import *

import spotipy.util as util
import youtube_dl


def authenticate():
    return util.prompt_for_user_token(username,scope, CLIENT_ID, CLIENT_SECRET, REDIRECT_URL)


def fetch_tracks(sp, playlist):
    log.debug('Fetching saved tracks')
    offset = 0
    songs = []
    current_user_id = sp.current_user()['id']
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
    with open('songs.txt', 'w') as f:
        f.write('\n'.join(songs))
    f.close()


def download_songs(songs,download_directory):
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

