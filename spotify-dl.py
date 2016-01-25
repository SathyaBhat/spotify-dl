#!/usr/bin/env python

from scaffold import *
from spotify import authenticate
from spotify import fetch_saved_tracks
from spotify import save_songs_to_file
from spotify import download_songs
from youtube import fetch_youtube_url
import spotipy
import argparse

if __name__ == '__main__':
    log.info('Starting spotify-dl')

    parser = argparse.ArgumentParser(prog='spotify-dl')
    parser.add_argument('-d', '--download', action='store_true', help='Download using youtube-dl')
    parser.add_argument('-V', '--verbose', action='store_true', help='Show more information on what''s happening.')
    args = parser.parse_args()
    if args.verbose:
        log.setLevel(logging.DEBUG)

    token = authenticate()
    sp = spotipy.Spotify(auth=token)
    songs = fetch_saved_tracks(sp)
    url = []
    for s in songs:
        link = fetch_youtube_url(s)
        if link:
            url.append(link)
    save_songs_to_file(url)
    if args.download == True:
        download_songs(url)
