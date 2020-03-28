#!/usr/bin/env python
import os
import re
from logging import DEBUG
import argparse
import json
import spotipy

from spotify_dl.scaffold import *
from spotify_dl.spotify import authenticate
from spotify_dl.spotify import fetch_tracks
from spotify_dl.spotify import save_songs_to_file
from spotify_dl.spotify import download_songs
from spotify_dl.spotify import playlist_name
from spotify_dl.youtube import fetch_youtube_url
from spotify_dl.spotify import extract_user_and_playlist_from_uri
from spotify_dl.spotify import get_playlist_name_from_id
from spotify_dl.constants import VERSION
from spotify_dl.youtube import get_youtube_dev_key

def spotify_dl():
    parser = argparse.ArgumentParser(prog='spotify_dl')
    parser.add_argument('-d', '--download', action='store_true',
                        help='Download using youtube-dl', default=True)
    parser.add_argument('-p', '--playlist', action='store',
                        help='Download from playlist id instead of'
                        ' saved tracks')
    parser.add_argument('-V', '--verbose', action='store_true',
                        help='Show more information on what''s happening.')
    parser.add_argument('-v', '--version', action='store_true',
                        help='Shows current version of the program')
    parser.add_argument('-o', '--output', type=str, action='store',
                        help='Specify download directory.')
    parser.add_argument('-u', '--user_id', action='store',
                        help='Specify the playlist owner\'s userid when it'
                        ' is different than your spotify userid')
    parser.add_argument('-i', '--uri', type=str, action='store',
                        nargs='*', help='Given a URI, download it.')
    parser.add_argument('-f', '--format_str', type=str, action='store',
                        help='Specify youtube-dl format string.',
                        default='bestaudio/best')
    parser.add_argument('-m', '--skip_mp3', action='store_true',
                        help='Don\'t convert downloaded songs to mp3')
    parser.add_argument('-l', '--url', action="store",
                        help="Spotify Playlist link URL")

    args = parser.parse_args()

    playlist_url_pattern = re.compile(r'^https://open.spotify.com/(.+)$')

    if args.version:
        print("spotify_dl v{}".format(VERSION))
        exit(0)

    if os.path.isfile(os.path.expanduser('~/.spotify_dl_settings')):
        with open(os.path.expanduser('~/.spotify_dl_settings')) as file:
            config = json.loads(file.read())

        for key, value in config.items():
            if value and (value.lower() == 'true' or value.lower() == 't'):
                setattr(args, key, True)
            else:
                setattr(args, key, value)

    if args.verbose:
        log.setLevel(DEBUG)

    log.info('Starting spotify_dl')
    log.debug('Setting debug mode on spotify_dl')

    if not check_for_tokens():
        exit(1)

    token = authenticate()
    sp = spotipy.Spotify(auth=token)
    log.debug('Arguments: {}'.format(args))

    if args.url:
        url_match = playlist_url_pattern.match(args.url)
        if url_match and len(url_match.groups()) > 0:
            uri = "spotify:" + url_match.groups()[0].replace('/', ':')
            args.uri = [uri]
        else:
            raise Exception('Invalid playlist URL ')
    if args.uri:
        current_user_id, playlist_id = extract_user_and_playlist_from_uri(args.uri[0], sp)
    else:
        if args.user_id is None:
            current_user_id = sp.current_user()['id']
        else:
            current_user_id = args.user_id

    if args.output:
        if args.uri:
            uri = args.uri[0]
            playlist = playlist_name(uri, sp)
        else:
            playlist = get_playlist_name_from_id(args.playlist, current_user_id, sp)

        log.info("Saving songs to: {}".format(playlist))
        download_directory = args.output + '/' + playlist
        if len(download_directory) >= 0 and download_directory[-1] != '/':
            download_directory += '/'

        if not os.path.exists(download_directory):
            os.makedirs(download_directory)
    else:
        download_directory = ''

    if args.uri:
        songs = fetch_tracks(sp, playlist_id, current_user_id)
    else:
        songs = fetch_tracks(sp, args.playlist, current_user_id)
    url = []
    for song, artist in songs.items():
        link = fetch_youtube_url(song + ' - ' + artist, get_youtube_dev_key())
        if link:
            url.append((link, song, artist))

    save_songs_to_file(url, download_directory)
    if args.download is True:
        download_songs(url, download_directory, args.format_str, args.skip_mp3)


if __name__ == '__main__':
    spotify_dl()
