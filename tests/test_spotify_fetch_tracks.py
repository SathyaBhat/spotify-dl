from spotipy.oauth2 import SpotifyClientCredentials
from spotify_dl.spotify import fetch_tracks
import spotipy


def spotify_auth():
    client = spotipy.Spotify(auth_manager=SpotifyClientCredentials())
    return client


def test_spotify_playlist_fetch_one():
    sp = spotify_auth()
    url = "https://open.spotify.com/playlist/1EqaIF6DswCUE0I6gAzQQv?si=9BzJyGNRSGOZ-nsL66WmmA"
    item_type = "playlist"
    songs = fetch_tracks(sp, item_type, url)
    assert {'name': 'Hotel California - Live On MTV, 1994', 'artist': 'Eagles',
            'album': 'Hell Freezes Over (Remaster 2018)', 'year': '1994', 'num_tracks': 15, 'num': 6} == songs[0]


def test_spotify_playlist_fetch_more():
    sp = spotify_auth()
    url = "https://open.spotify.com/playlist/3cEYpjA9oz9GiPac4AsH4n"
    item_type = "playlist"
    songs = fetch_tracks(sp, item_type, url)
    assert {'name': 'Api', 'artist': 'Odiseo', 'album': 'Progressive Psy Trance Picks Vol.8', 'year': '2012', 'num_tracks': 20, 'num': 10} \
           == songs[0]
    assert {'name': 'Is', 'artist': 'Vlasta Marek', 'album': 'Wellness & Dreaming Source', 'year': '2015', 'num_tracks': 25, 'num': 21} \
           == songs[1]
    assert {'name': 'All I Want', 'artist': 'LCD Soundsystem', 'album': 'This Is Happening', 'year': '2010', 'num_tracks': 9, 'num': 4} \
           == songs[2]
    assert {'name': 'Endpoints', 'artist': 'Glenn Horiuchi Trio', 'album': 'Glenn Horiuchi Trio / Gelenn Horiuchi Quartet: Mercy / '
                                                         'Jump Start / Endpoints / Curl Out / Earthworks / Mind Probe / '
                                                         'Null Set / Another Space (A)', 'year': '2011',
            'num_tracks': 8, 'num': 2} \
           == songs[3]
    assert {'name': 'You Are So Beautiful', 'artist': 'Zucchero', 'album': 'All The Best (Spanish Version)', 'year': '2007',
            'num_tracks': 18, 'num': 18} \
           == songs[4]


def test_spotify_track_fetch_one():
    sp = spotify_auth()
    url = "https://open.spotify.com/track/2GpBrAoCwt48fxjgjlzMd4?si=xzZIHC5hSGuSEAXXkxgKiw"
    item_type = "track"
    songs = fetch_tracks(sp, item_type, url)
    assert {'name': 'Hotel California - Live On MTV, 1994', 'artist': 'Eagles', 'album': 'Hell Freezes Over (Remaster 2018)',
            'year': '1994', 'num_tracks': 15, 'num': 6} == songs[0]


def test_spotify_album_fetch_one():
    sp = spotify_auth()
    url = "https://open.spotify.com/album/1IVEQdX6Y37za9PMB0afPX?si=Hz8CMaYpTx2O0PeuDglKaA"
    item_type = "album"
    songs = fetch_tracks(sp, item_type, url)
    assert {'name': 'Simple Song', 'artist': 'The Shins', 'album': 'Simple Song', 'year': '2012', 'num_tracks': 1,
            'num': 1} == songs[0]


def test_spotify_album_fetch_more():
    sp = spotify_auth()
    url = "https://open.spotify.com/album/2RKEso6nin3nhRyAd36Omv?si=KEBaFQxYR9-nRJLarH2QNQ"
    item_type = "album"
    songs = fetch_tracks(sp, item_type, url)
    assert [{'name': 'Procession - Remastered 2011', 'artist': 'Queen', 'album': 'Queen II (Deluxe Remastered Version)',
             'year': '1974', 'num_tracks': 16, 'num': 1},
            {'name': 'Father To Son - Remastered 2011', 'artist': 'Queen', 'album': 'Queen II (Deluxe Remastered Version)',
             'year': '1974', 'num_tracks': 16, 'num': 2},
            {'name':'White Queen (As It Began) - Remastered 2011', 'artist': 'Queen', 'album': 'Queen II (Deluxe Remastered Version)',
             'year': '1974', 'num_tracks': 16, 'num': 3},
            {'name': 'Some Day One Day - Remastered 2011', 'artist': 'Queen',
              'album': 'Queen II (Deluxe Remastered Version)', 'year': '1974', 'num_tracks': 16, 'num': 4},
            {'name': 'The Loser In The End - Remastered 2011', 'artist': 'Queen', 'album': 'Queen II (Deluxe Remastered Version)',
             'year': '1974', 'num_tracks': 16, 'num': 5},
            {'name':'Ogre Battle - Remastered 2011', 'artist': 'Queen', 'album': 'Queen II (Deluxe Remastered Version)',
             'year': '1974', 'num_tracks': 16, 'num': 6},
            {'name': "The Fairy Feller's Master-Stroke - Remastered 2011", 'artist': 'Queen',
             'album': 'Queen II (Deluxe Remastered Version)', 'year': '1974', 'num_tracks': 16, 'num': 7},
            {'name':'Nevermore - Remastered 2011', 'artist': 'Queen', 'album': 'Queen II (Deluxe Remastered Version)',
             'year': '1974', 'num_tracks': 16, 'num': 8},
            {'name':'The March Of The Black Queen - Remastered 2011', 'artist': 'Queen',
             'album': 'Queen II (Deluxe Remastered Version)', 'year': '1974', 'num_tracks': 16, 'num': 9},
            {'name': 'Funny How Love Is - Remastered 2011', 'artist': 'Queen',
             'album': 'Queen II (Deluxe Remastered Version)',
             'year': '1974', 'num_tracks': 16, 'num': 10},
            {'name':'Seven Seas Of Rhye - Remastered 2011', 'artist': 'Queen',
              'album': 'Queen II (Deluxe Remastered Version)', 'year': '1974', 'num_tracks': 16, 'num': 11},
            {'name': "See What A Fool I've Been - Live BBC Session, London / July 1973 / 2011 Remix",
             'artist': 'Queen',
             'album': 'Queen II (Deluxe Remastered Version)', 'year': '1974', 'num_tracks': 16, 'num': 1},
            {'name': 'White Queen (As It Began) - Live At Hammersmith Odeon, London / December 1975', 'artist': 'Queen',
             'album': 'Queen II (Deluxe Remastered Version)', 'year': '1974', 'num_tracks': 16, 'num': 2},
            {'name': 'Seven Seas Of Rhye - Instrumental Mix 2011', 'artist': 'Queen', 'album': 'Queen II (Deluxe Remastered Version)',
             'year': '1974', 'num_tracks': 16, 'num': 3},
            {'name': 'Nevermore - Live BBC Session, London / April 1974', 'artist': 'Queen',
             'album': 'Queen II (Deluxe Remastered Version)', 'year': '1974', 'num_tracks': 16, 'num': 4},
            {'name' : 'See What A Fool I’ve Been - B-Side Version / Remastered 2011', 'artist': 'Queen',
             'album': 'Queen II (Deluxe Remastered Version)', 'year': '1974', 'num_tracks': 16, 'num': 5}] == songs
    assert (len(songs)) == 16
