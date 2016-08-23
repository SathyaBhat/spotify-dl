from __future__ import unicode_literals
from spotify_dl.scaffold import *
import spotipy.util as util
import youtube_dl
import re
import os


def authenticate():
    """Authenticates you to Spotify
    """
    scope = 'user-library-read'
    username = ''
    return util.prompt_for_user_token(username, scope)


def fetch_tracks(sp, playlist, user_id):
    """Fetches tracks from Spotify user's saved
        tracks or from playlist(if playlist parameter is passed
        and saves song name and artist name to songs list
    """
    log.debug('Fetching saved tracks')
    offset = 0
    songs_dict = {}
    if user_id is None:
        current_user_id = sp.current_user()['id']
    else:
        current_user_id = user_id
    while True:
        if playlist is None:
            results = sp.current_user_saved_tracks(limit=50, offset=offset)
        else:
            results = sp.user_playlist_tracks(current_user_id, playlist, None,
                                              limit=50, offset=offset)

        log.debug('Got result json {}'.format(results))
        for item in results['items']:
            track = item['track']
            track_name = str(track['name'])
            track_artist = str(track['artists'][0]['name'])
            log.debug('Appending {} to'
                      'songs list'.format(track['name'] + ' - ' +
                                          track['artists'][0]['name']))
            songs_dict.update({track_name: track_artist})
            offset += 1

        if results.get('next') is None:
            log.info('All pages fetched, time to leave.'
                     ' Added {} songs in total'.format(offset))
            break
    return songs_dict


def save_songs_to_file(songs, directory):
    """
    :param songs
    Saves the songs fetched from fetch_tracks function to songs.txt file
       to be downloaded from youtube-dl
    """

    with open(os.path.join(directory, 'songs.txt'), 'w') as f:
        f.write(' '.join(str(songs)))
    f.close()


def download_songs(info, download_directory):
    """
    Downloads songs from the YouTube URL passed to either
       current directory or download_directory, is it is passed
    """
    for item in info:
        log.debug('Songs to download: {}'.format(item))
        url_, track_, artist_ = item
        download_archive = download_directory + 'downloaded_songs.txt'
        outtmpl = download_directory + '%(title)s.%(ext)s'
        ydl_opts = {
            'format': 'bestaudio/best',
            'download_archive': download_archive,
            'outtmpl': outtmpl,
            'noplaylist': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            },
                {'key': 'FFmpegMetadata'},
            ],
            'postprocessor_args': ['-metadata', 'title=' + str(track_)],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                log.debug(ydl.download([url_]))
            except Exception as e:
                log.debug(e)
                print('Failed to download: {}'.format(url_))
                continue


def extract_user_and_playlist_from_uri(uri):
    playlist_re = re.compile("spotify:user:[\w,.]+:playlist:[\w]+")
    for playlist_uri in playlist_re.findall(uri):
        segments = playlist_uri.split(":")
        user_id = segments[2]
        log.info('List owner: ' + str(user_id))
        playlist_id = segments[4]
        log.info('List ID: ' + str(playlist_id))
    return user_id, playlist_id


def playlist_name(uri, sp):
    user_id, playlist_id = extract_user_and_playlist_from_uri(uri)
    playlist = sp.user_playlist(user_id, playlist_id,
                                fields="tracks, next, name")
    name = playlist['name']
    return name
