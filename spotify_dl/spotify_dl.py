#!/usr/bin/env python3
import argparse
import json
import os
import sys
from logging import DEBUG
from pathlib import Path, PurePath
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from spotify_dl.constants import VERSION
from spotify_dl.scaffold import log, check_for_tokens, console
from spotify_dl.spotify import fetch_tracks, parse_spotify_url, validate_spotify_url, get_item_name
from spotify_dl.youtube import download_songs, default_filename, playlist_num_filename


def spotify_dl():
    """Main entry point of the script."""
    parser = argparse.ArgumentParser(prog='spotify_dl')
    parser.add_argument('-l', '--url', action="store",
                        help="Spotify Playlist link URL", type=str, nargs='+', required=True)
    parser.add_argument('-o', '--output', type=str, action='store',
                        help='Specify download directory.', required=False)
    parser.add_argument('-d', '--download', action='store_true',
                        help='Download using youtube-dl', default=True)
    parser.add_argument('-f', '--format_str', type=str, action='store',
                        help='Specify youtube-dl format string.',
                        default='bestaudio/best')
    parser.add_argument('-k', '--keep_playlist_order', default=False,
                        action='store_true',
                        help='Whether to keep original playlist ordering or not.')
    parser.add_argument('-m', '--skip_mp3', action='store_true',
                        help='Don\'t convert downloaded songs to mp3')
    parser.add_argument('-w', '--no-overwrites', action='store_true',
                        help="Whether we should avoid overwriting the target audio file if it already exists",
                        default=False)
    parser.add_argument('-V', '--verbose', action='store_true',
                        help='Show more information on what''s happening.')
    parser.add_argument('-v', '--version', action='store_true',
                        help='Shows current version of the program')
    args = parser.parse_args()

    if args.version:
        console.print(f"spotify_dl [bold green]v{VERSION}[/bold green]")
        sys.exit(0)

    if os.path.isfile(os.path.expanduser('~/.spotify_dl_settings')):
        with open(os.path.expanduser('~/.spotify_dl_settings')) as file:
            config = json.loads(file.read())

        for key, value in config.items():
            if (isinstance(value, bool) and value) or (isinstance(value, str) and value and value.lower() in ['true', 't']):
                setattr(args, key, True)
            else:
                setattr(args, key, value)

    if args.verbose:
        log.setLevel(DEBUG)

    if not hasattr(args, 'url'):
        raise(Exception("No playlist url provided"))
    if not hasattr(args, 'output'):
        raise(Exception("No output folder configured"))

    console.log(f"Starting spotify_dl [bold green]v{VERSION}[/bold green]")
    log.debug('Setting debug mode on spotify_dl')

    if not check_for_tokens():
        sys.exit(1)

    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())
    log.debug('Arguments: {}'.format(args))

    for url in args.url:
        if url:
            valid_item = validate_spotify_url(url)

        if not valid_item:
            sys.exit(1)

        if args.output:
            item_type, item_id = parse_spotify_url(url)
            directory_name = get_item_name(sp, item_type, item_id)
            save_path = Path(PurePath.joinpath(Path(args.output), Path(directory_name)))
            save_path.mkdir(parents=True, exist_ok=True)
            console.print(f"Saving songs to [bold green]{directory_name}[/bold green] directory")

        songs = fetch_tracks(sp, item_type, url)
        if args.download is True:
            file_name_f = default_filename
            if args.keep_playlist_order:
                file_name_f = playlist_num_filename

            download_songs(songs, save_path, args.format_str, args.skip_mp3, args.keep_playlist_order, args.no_overwrites, file_name_f)


if __name__ == '__main__':
    spotify_dl()
