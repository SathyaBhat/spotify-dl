import os
import urllib
import urllib.request
from pathlib import Path
from mutagen.easyid3 import EasyID3
from mutagen.id3 import APIC, ID3
from mutagen.mp3 import MP3

from spotify_dl import youtube as yt


def test_download_one_false_skip():

    songs = {
        "urls": [
            {
                "save_path": Path("Hotel California - Live On MTV, 1994"),
                "songs": [
                    {
                        "name": "Hotel California - Live On MTV, 1994",
                        "artist": "Eagles",
                        "album": "Hell Freezes Over (Remaster 2018)",
                        "year": "1994",
                        "num_tracks": 15,
                        "num": 6,
                        "track_url": None,
                        "playlist_num": 1,
                        "cover": "https://i.scdn.co/image/ab67616d0000b27396d28597a5ae44ab66552183",
                        "genre": "album rock",
                        "spotify_id": "2GpBrAoCwt48fxjgjlzMd4",
                        'tempo': 74.656,
                    }
                ],
            }
        ]
    }

    yt.download_songs(
        songs=songs,
        output_dir=os.path.dirname(os.path.realpath(__file__)),
        format_string="best",
        skip_mp3=False,
        keep_playlist_order=False,
        no_overwrites=False,
        remove_trailing_tracks=False,
        use_sponsorblock="no",
        file_name_f=yt.default_filename,
        multi_core=0,
    )
    music = MP3(
        "Hotel California - Live On MTV, 1994/Eagles - Hotel California - Live On MTV, 1994.mp3",
        ID3=EasyID3,
    )
    tags = ID3(
        "Hotel California - Live On MTV, 1994/Eagles - Hotel California - Live On MTV, 1994.mp3"
    )
    assert music["artist"][0] == "Eagles"
    assert music["album"][0] == "Hell Freezes Over (Remaster 2018)"
    assert music["genre"][0] == "album rock"
    assert tags.getall("APIC")[0] == APIC(
        encoding=3,
        mime="image/jpeg",
        type=3,
        desc="Cover",
        data=urllib.request.urlopen(songs["urls"][0]["songs"][0].get("cover")).read(),
    )


def test_download_one_true_skip():
    songs = {
        "urls": [
            {
                "save_path": Path("Hotel California - Live On MTV, 1994"),
                "songs": [
                    {
                        "name": "Hotel California - Live On MTV, 1994",
                        "artist": "Eagles",
                        "album": "Hell Freezes Over (Remaster 2018)",
                        "year": "1994",
                        "num_tracks": 15,
                        "num": 6,
                        "track_url": None,
                        "playlist_num": 1,
                        "cover": "https://i.scdn.co/image/ab67616d0000b27396d28597a5ae44ab66552183",
                        "genre": "album rock",
                        "spotify_id": "2GpBrAoCwt48fxjgjlzMd4",
                        'tempo': 74.656,
                    }
                ],
            }
        ]
    }
    yt.download_songs(
        songs=songs,
        output_dir=os.path.dirname(os.path.realpath(__file__)),
        format_string="best",
        skip_mp3=True,
        keep_playlist_order=False,
        no_overwrites=False,
        remove_trailing_tracks=False,
        use_sponsorblock="yes",
        file_name_f=yt.default_filename,
        multi_core=0,
    )


def test_download_cover_none():
    songs = {
        "urls": [
            {
                "save_path": Path("The Fairy Feller's Master-Stroke - Remastered 2011"),
                "songs": [
                    {
                        "name": "The Fairy Feller's Master-Stroke - Remastered 2011",
                        "artist": "Queen",
                        "album": "Queen II (Deluxe Edition 2011 Remaster)",
                        "year": "1974",
                        "track_url": None,
                        "num_tracks": 16,
                        "num": 7,
                        "playlist_num": 1,
                        "cover": None,
                        "genre": "classic rock",
                        "spotify_id": "12LhScrlYazmU4vsqpRQNI",
                        'tempo': 159.15,
                    }
                ],
            }
        ]
    }
    yt.download_songs(
        songs=songs,
        output_dir=os.path.dirname(os.path.realpath(__file__)),
        format_string="best",
        skip_mp3=False,
        keep_playlist_order=False,
        no_overwrites=False,
        remove_trailing_tracks=False,
        use_sponsorblock="no",
        file_name_f=yt.default_filename,
        multi_core=0,
    )

    music = MP3(
        "The Fairy Feller's Master-Stroke - Remastered 2011/Queen - The Fairy Feller's Master-Stroke - Remastered 2011.mp3",
        ID3=EasyID3,
    )
    tags = ID3(
        "The Fairy Feller's Master-Stroke - Remastered 2011/Queen - The Fairy Feller's Master-Stroke - Remastered 2011.mp3"
    )
    assert music["artist"][0] == "Queen"
    assert music["album"][0] == "Queen II (Deluxe Edition 2011 Remaster)"
    assert music["genre"][0] == "classic rock"
    assert len(tags.getall("APIC")) == 0
