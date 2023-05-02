#!/usr/bin/env python3
import argparse
import time
import json
import os
import sys
from logging import DEBUG, ERROR
from pathlib import Path, PurePath
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from spotify_dl.constants import VERSION
from spotify_dl.scaffold import log, setLogLevel, console, get_tokens
from spotify_dl.spotify import (
    fetch_tracks,
    parse_spotify_url,
    validate_spotify_urls,
    get_item_name,
)

from spotify_dl.youtube import download_songs, default_filename, playlist_num_filename, dump_json


def spotify_dl():
    """Main entry point of the script."""
    parser = argparse.ArgumentParser(prog="spotify_dl")
    parser.add_argument(
        "-l",
        "--url",
        action="store",
        help="Spotify Playlist link URL",
        type=str,
        nargs="+",
        required=False,  # this has to be set to false to prevent useless prompt for url when all user wants is the script version
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        action="store",
        help="Specify download directory.",
        required=False,
        default=".",
    )
    parser.add_argument(
        "-d",
        "--download",
        action="store_true",
        help="Download using youtube-dl",
        default=True,
    )
    parser.add_argument(
        "-j",
        "--dump-json",
        action="store_true",
        help="Dump info-json using youtube-dl",
        default=False
    )
    parser.add_argument(
        "-f",
        "--format_str",
        type=str,
        action="store",
        help="Specify youtube-dl format string.",
        default="bestaudio/best",
    )
    parser.add_argument(
        "-k",
        "--keep_playlist_order",
        default=False,
        action="store_true",
        help="Whether to keep original playlist ordering or not.",
    )
    parser.add_argument(
        "-m",
        "--skip_mp3",
        action="store_true",
        help="Don't convert downloaded songs to mp3",
    )
    parser.add_argument(
        "-s",
        "--use_sponsorblock",
        default="no",
        action="store",
        help="Whether to skip non-music sections using SponsorBlock API. Pass y or yes to skip using SponsorBlock",
    )
    parser.add_argument(
        "-w",
        "--no-overwrites",
        action="store_true",
        help="Whether we should avoid overwriting the target audio file if it already exists",
        default=False,
    )
    parser.add_argument(
        "-r",
        "--remove-trailing-tracks",
        default="no",
        action="store_true",
        help="Whether we should delete tracks that were previously downloaded but are not longer in the playlist"
    )
    parser.add_argument(
        "-V",
        "--verbose",
        action="store_true",
        help="Show more information on what" "s happening.",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="Shows current version of the program",
    )
    parser.add_argument(
        "-mc",
        "--multi_core",
        action="store",
        type=str,
        default=0,
        help="Use multiprocessing [-m [int:numcores]",
    )
    parser.add_argument(
        "-p",
        "--proxy",
        action="store",
        type=str,
        default="",
        help="Download through a proxy. Support HTTP & SOCKS5. Use 'http://username:password@hostname:port' or 'http://hostname:port'",
    )
    args = parser.parse_args()
    num_cores = os.cpu_count()
    args.multi_core = int(args.multi_core)

    if args.dump_json:
        setLogLevel(ERROR)
    if args.verbose:
        setLogLevel(DEBUG)

    log.info("Starting spotify_dl v%s", VERSION)
    log.debug("Setting debug mode on spotify_dl")

    if args.multi_core > (num_cores - 1):
        log.info(
            "Requested cores %d exceeds available %d, using %d cores.",
            args.multi_core,
            num_cores,
            num_cores - 1
        )
        args.multi_core = num_cores - 1
    if args.version:
        console.print(f"spotify_dl [bold green]v{VERSION}[/bold green]")
        sys.exit(0)

    if os.path.isfile(os.path.expanduser("~/.spotify_dl_settings")):
        with open(os.path.expanduser("~/.spotify_dl_settings")) as file:
            config = json.load(file)
            print(config)

        for key, value in config.items():
            if (isinstance(value, bool) and value) or (
                isinstance(value, str) and value and value.lower() in ["true", "t"]
            ):
                setattr(args, key, True)
            else:
                setattr(args, key, value)

    if not args.url:
        raise (Exception("No playlist url provided:"))

    tokens = get_tokens()
    if tokens is None:
        sys.exit(1)
    client_id, client_secret = tokens

    sp = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id=client_id, client_secret=client_secret
        )
    )
    log.debug("Arguments: %s ", args)
    log.info(
        "Sponsorblock enabled?: %s",
        args.use_sponsorblock
    )
    valid_urls = validate_spotify_urls(args.url)
    if not valid_urls:
        sys.exit(1)

    url_data = {"urls": []}

    for url in valid_urls:
        url_dict = {}
        item_type, item_id = parse_spotify_url(url)
        directory_name = get_item_name(sp, item_type, item_id)
        url_dict["save_path"] = Path(
            PurePath.joinpath(Path(args.output), Path(directory_name))
        )
        url_dict["save_path"].mkdir(parents=True, exist_ok=True)
        log.info(
            "Saving songs to %s directory",
            directory_name
        )
        url_dict["songs"] = fetch_tracks(sp, item_type, url)
        url_data["urls"].append(url_dict.copy())
    if args.dump_json is True:
        dump_json(url_dict["songs"])
    elif args.download is True:
        file_name_f = default_filename
        if args.keep_playlist_order:
            file_name_f = playlist_num_filename

        download_songs(
            songs=url_data,
            output_dir=args.output,
            format_str=args.format_str,
            skip_mp3=args.skip_mp3,
            keep_playlist_order=args.keep_playlist_order,
            no_overwrites=args.no_overwrites,
            remove_trailing_tracks=args.remove_trailing_tracks,
            use_sponsorblock=args.use_sponsorblock,
            file_name_f=file_name_f,
            multi_core=args.multi_core,
            proxy=args.proxy,
        )


if __name__ == "__main__":
    start_time = time.time()
    spotify_dl()
    log.info(
        "Download completed in %f seconds.", 
        time.time() - start_time
    )
