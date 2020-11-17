#!/usr/bin/env python
import os
from logging import DEBUG
import argparse
import json
import spotipy
import sys

from spotify_dl.scaffold import log, check_for_tokens
from spotify_dl.spotify import fetch_tracks, parse_spotify_url, validate_spotify_url, get_item_name
from spotify_dl.youtube import download_songs
from spotify_dl.constants import VERSION
from spotify_dl.models import db, Song
from spotipy.oauth2 import SpotifyClientCredentials
from pathlib import Path, PurePath


def spotify_dl():
    """Main entry point of the script."""
    parser = argparse.ArgumentParser(prog='spotify_dl')
    parser.add_argument('-l', '--url', action="store",
                        help="Spotify Playlist link URL", type=str, required=True)
    parser.add_argument('-o', '--output', type=str, action='store',
                        help='Specify download directory.', required=True)
    parser.add_argument('-d', '--download', action='store_true',
                        help='Download using youtube-dl', default=True)
    parser.add_argument('-f', '--format_str', type=str, action='store',
                        help='Specify youtube-dl format string.',
                        default='bestaudio/best')
    parser.add_argument('-m', '--skip_mp3', action='store_true',
                        help='Don\'t convert downloaded songs to mp3')
    parser.add_argument('-s', '--scrape', action="store",
                        help="Use HTML Scraper for YouTube Search", default=True)
    parser.add_argument('-V', '--verbose', action='store_true',
                        help='Show more information on what''s happening.')
    parser.add_argument('-v', '--version', action='store_true',
                        help='Shows current version of the program')
    args = parser.parse_args()

    if args.version:
        print("spotify_dl v{}".format(VERSION))
        exit(0)

    db.connect()
    db.create_tables([Song])
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

    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())
    log.debug('Arguments: {}'.format(args))

    if args.url:
        valid_item = validate_spotify_url(args.url)

    if not valid_item:
        sys.exit(1)

    if args.output:
        item_type, item_id = parse_spotify_url(args.url)
        directory_name = get_item_name(sp, item_type, item_id)
        save_path = Path(PurePath.joinpath(Path(args.output), Path(directory_name)))
        save_path.mkdir(parents=True, exist_ok=True)
        log.info("Saving songs to: {}".format(directory_name))

    songs = fetch_tracks(sp, item_type, args.url)
    if args.download is True:
        download_songs(songs, str(save_path), args.format_str, args.skip_mp3)


if __name__ == '__main__':
    spotify_dl()
