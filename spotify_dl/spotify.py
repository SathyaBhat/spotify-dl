from __future__ import unicode_literals
import re

import youtube_dl

from spotify_dl.scaffold import *

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

        log.debug(f'Got result json keys {results.keys()}', )
        for item in results['tracks']['items']:
            track = item['track']

            if track is not None:
                track_name = str(track['name'])
                track_artist = str(track['artists'][0]['name'])
                log.debug('Appending %s to'
                        'songs list', (track['name'] + ' - ' + track['artists'][0]['name']))
                songs_dict.update({track_name: track_artist})
            else:
                log.warning("Track/artist name for %s not found, skipping", track)

            offset += 1

        if results.get('next') is None:
            log.info('All pages fetched, time to leave.'
                     ' Added %s songs in total', offset)
            break
    return songs_dict


def download_songs(info, download_directory, format_string, skip_mp3):
    """
    Downloads songs from the YouTube URL passed to either
       current directory or download_directory, is it is passed
    """
    for number, item in enumerate(info):
        log.debug('Songs to download: %s', item)
        url_, track_, artist_ = item
        download_archive = download_directory + 'downloaded_songs.txt'
        outtmpl = download_directory + '%(title)s.%(ext)s'
        ydl_opts = {
            'format': format_string,
            'download_archive': download_archive,
            'outtmpl': outtmpl,
            'noplaylist': True,
            'postprocessor_args': ['-metadata', 'title=' + str(track_),
                                   '-metadata', 'artist=' + str(artist_),
                                   '-metadata', 'track=' + str(number + 1)]
        }
        if not skip_mp3:
            mp3_postprocess_opts = {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }
            ydl_opts['postprocessors'] = [mp3_postprocess_opts.copy()]

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                log.debug(ydl.download([url_]))
            except Exception as e:
                log.debug(e)
                print('Failed to download: {}'.format(url_))
                continue

def parse_spotify_url(url):
    parsed_url = url.replace("https://open.spotify.com/","")
    type = parsed_url.split("/")[0]
    id = parsed_url.split("/")[1]
    return type, id

def get_item_name(sp, item_type, id):

    # TODO: Find better way to call this?
    if item_type == 'playlist':
        name = sp.playlist(playlist_id=id, fields='name').get('name')

    if item_type == 'album':
        name = sp.album(album_id=id).get('name')

    if item_type == 'track':
        name = sp.track(track_id=id).get('name')
    
    return name