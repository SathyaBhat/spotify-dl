from spotipy.oauth2 import SpotifyClientCredentials
from spotify_dl.spotify import fetch_tracks
import spotipy
import base64

def spotify_auth():
    # test client ids, b64 for just to deter. 
    client = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=base64.b64decode('NjliZDE4ZjNiNDY3NGMyNTkwNTllMzE5YTQ1ZGQwMzY=').decode('ascii'),
                                                                    client_secret=base64.b64decode('NTczY2UwYmM2OWUzNDdkNzg3NjgwZDBlMzJmOTQ3MGM=').decode('ascii')))
    return client


def test_spotify_playlist_fetch_one():
    sp = spotify_auth()
    url = "https://open.spotify.com/playlist/1EqaIF6DswCUE0I6gAzQQv?si=9BzJyGNRSGOZ-nsL66WmmA"
    item_type = "playlist"
    songs = fetch_tracks(sp, item_type, url)
    assert {'album': 'Hell Freezes Over (Remaster 2018)',
             'artist': 'Eagles',
             'cover': 'https://i.scdn.co/image/ab67616d0000b27396d28597a5ae44ab66552183',
             'genre': 'album rock',
             'name': 'Hotel California - Live On MTV, 1994',
             'num': 6,
             'num_tracks': 15,
             'year': '1994',
             'playlist_num': 1,
             'spotify_id': '2GpBrAoCwt48fxjgjlzMd4'} == songs[0]

    
def test_spotify_playlist_fetch_more():
    sp = spotify_auth()
    url = "https://open.spotify.com/playlist/3cEYpjA9oz9GiPac4AsH4n"
    item_type = "playlist"
    songs = fetch_tracks(sp, item_type, url)
    assert [{'album': 'Progressive Psy Trance Picks Vol.8',
              'artist': 'Odiseo',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273ce6d0eef0c1ce77e5f95bbbc',
              'genre': 'progressive psytrance',
              'name': 'Api',
              'num': 10,
              'num_tracks': 20,
              'year': '2012',
              'playlist_num': 1,
              'spotify_id': '4rzfv0JLZfVhOhbSQ8o5jZ'},
             {'album': 'Wellness & Dreaming Source',
              'artist': 'Vlasta Marek',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273aa2ff29970d9a63a49dfaeb2',
              'genre': 'singing bowl',
              'name': 'Is',
              'num': 21,
              'num_tracks': 25,
              'year': '2015',
              'playlist_num': 2,
              'spotify_id': '5o3jMYOSbaVz3tkgwhELSV'},
             {'album': 'This Is Happening',
              'artist': 'LCD Soundsystem',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273ee0d0dce888c6c8a70db6e8b',
              'genre': 'alternative dance',
              'name': 'All I Want',
              'num': 4,
              'num_tracks': 9,
              'year': '2010',
              'playlist_num': 3,
              'spotify_id': '4Cy0NHJ8Gh0xMdwyM9RkQm'},
             {'album': 'Glenn Horiuchi Trio / Gelenn Horiuchi Quartet: Mercy / Jump Start '
                       '/ Endpoints / Curl Out / Earthworks / Mind Probe / Null Set / '
                       'Another Space (A)',
              'artist': 'Glenn Horiuchi Trio',
              'cover': 'https://i.scdn.co/image/ab67616d0000b2738b7447ac3daa1da18811cf7b',
              'genre': '',
              'name': 'Endpoints',
              'num': 2,
              'num_tracks': 8,
              'year': '2011',
              'playlist_num': 4,
              'spotify_id': '6hvFrZNocdt2FcKGCSY5NI'},
             {'album': 'All The Best (Spanish Version)',
              'artist': 'Zucchero',
              'cover': 'https://i.scdn.co/image/ab67616d0000b27304e57d181ff062f8339d6c71',
              'genre': 'classic italian pop',
              'name': 'You Are So Beautiful',
              'num': 18,
              'num_tracks': 18,
              'year': '2007',
              'playlist_num': 5,
              'spotify_id': '2E2znCPaS8anQe21GLxcvJ'}] == songs


def test_spotify_track_fetch_one():
    sp = spotify_auth()
    url = "https://open.spotify.com/track/2GpBrAoCwt48fxjgjlzMd4?si=xzZIHC5hSGuSEAXXkxgKiw"
    item_type = "track"
    songs = fetch_tracks(sp, item_type, url)
    assert {'album': 'Hell Freezes Over (Remaster 2018)',
             'artist': 'Eagles',
             'cover': 'https://i.scdn.co/image/ab67616d0000b27396d28597a5ae44ab66552183',
             'genre': 'album rock',
             'name': 'Hotel California - Live On MTV, 1994',
             'num': 6,
             'num_tracks': 15,
             'year': '1994',
             'playlist_num': 1,
             'spotify_id': '2GpBrAoCwt48fxjgjlzMd4'} == songs[0]


def test_spotify_album_fetch_one():
    sp = spotify_auth()
    url = "https://open.spotify.com/album/1IVEQdX6Y37za9PMB0afPX?si=Hz8CMaYpTx2O0PeuDglKaA"
    item_type = "album"
    songs = fetch_tracks(sp, item_type, url)
    assert {'album': 'Simple Song',
             'artist': 'The Shins',
             'cover': 'https://i.scdn.co/image/ab67616d0000b2737f6f8d24f3bba324727d6021',
             'genre': 'albuquerque indie',
             'name': 'Simple Song',
             'num': 1,
             'num_tracks': 1,
             'year': '2012',
             'playlist_num': 1,
             'spotify_id': '5EoKQDGE2zxrTfRFZF52u5'} == songs[0]


def test_spotify_album_fetch_more():
    sp = spotify_auth()
    url = "https://open.spotify.com/album/2RKEso6nin3nhRyAd36Omv?si=KEBaFQxYR9-nRJLarH2QNQ"
    item_type = "album"
    songs = fetch_tracks(sp, item_type, url)
    assert [{'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'genre': 'classic rock',
              'name': 'Procession - Remastered 2011',
              'num': 1,
              'num_tracks': 16,
              'year': '1974',
              'playlist_num': 1,
              'spotify_id': '69Yw7H4bRIwfIxL0ZCZy8y'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'genre': 'classic rock',
              'name': 'Father To Son - Remastered 2011',
              'num': 2,
              'num_tracks': 16,
              'year': '1974',
              'playlist_num': 2,
              'spotify_id': '5GGSjXZeTgX9sKYBtl8K6U'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'genre': 'classic rock',
              'name': 'White Queen (As It Began) - Remastered 2011',
              'num': 3,
              'num_tracks': 16,
              'year': '1974',
              'playlist_num': 3,
              'spotify_id': '0Ssh20fuVhmasLRJ97MLnp'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'genre': 'classic rock',
              'name': 'Some Day One Day - Remastered 2011',
              'num': 4,
              'num_tracks': 16,
              'year': '1974',
              'playlist_num': 4,
              'spotify_id': '2LasW39KJDE4VH9hTVNpE2'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'genre': 'classic rock',
              'name': 'The Loser In The End - Remastered 2011',
              'num': 5,
              'num_tracks': 16,
              'year': '1974',
              'playlist_num': 5,
              'spotify_id': '6jXrIu3hWbmJziw34IHIwM'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'genre': 'classic rock',
              'name': 'Ogre Battle - Remastered 2011',
              'num': 6,
              'num_tracks': 16,
              'year': '1974',
              'playlist_num': 6,
              'spotify_id': '5dHmGuUeRgp5f93G69tox5'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'genre': 'classic rock',
              'name': "The Fairy Feller's Master-Stroke - Remastered 2011",
              'num': 7,
              'num_tracks': 16,
              'year': '1974',
              'playlist_num': 7,
              'spotify_id': '2KPj0oB7cUuHQ3FuardOII'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'genre': 'classic rock',
              'name': 'Nevermore - Remastered 2011',
              'num': 8,
              'num_tracks': 16,
              'year': '1974',
              'playlist_num': 8,
              'spotify_id': '34CcBjL9WqEAtnl2i6Hbxa'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'genre': 'classic rock',
              'name': 'The March Of The Black Queen - Remastered 2011',
              'num': 9,
              'num_tracks': 16,
              'year': '1974',
              'playlist_num': 9,
              'spotify_id': '1x9ak6LGIazLhfuaSIEkhG'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'genre': 'classic rock',
              'name': 'Funny How Love Is - Remastered 2011',
              'num': 10,
              'num_tracks': 16,
              'year': '1974',
              'playlist_num': 10,
              'spotify_id': '4CITL18Tos0PscW1amCK4j'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'genre': 'classic rock',
              'name': 'Seven Seas Of Rhye - Remastered 2011',
              'num': 11,
              'num_tracks': 16,
              'year': '1974',
              'playlist_num': 11,
              'spotify_id': '1e9Tt3nKBwRbuaU79kN3dn'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'genre': 'classic rock',
              'name': "See What A Fool I've Been - Live BBC Session, London / July 1973 / "
                      '2011 Remix',
              'num': 1,
              'num_tracks': 16,
              'year': '1974',
              'playlist_num': 12,
              'spotify_id': '0uHqoDT7J2TYBsJx6m4Tvi'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'genre': 'classic rock',
              'name': 'White Queen (As It Began) - Live At Hammersmith Odeon, London / '
                      'December 1975',
              'num': 2,
              'num_tracks': 16,
              'year': '1974',
              'playlist_num': 13,
              'spotify_id': '3MIueGYoNiyBNfi5ukDgAK'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'genre': 'classic rock',
              'name': 'Seven Seas Of Rhye - Instrumental Mix 2011',
              'num': 3,
              'num_tracks': 16,
              'year': '1974',
              'playlist_num': 14,
              'spotify_id': '34WAOFWdJ83a3YYrDAZTjm'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'genre': 'classic rock',
              'name': 'Nevermore - Live BBC Session, London / April 1974',
              'num': 4,
              'num_tracks': 16,
              'year': '1974',
              'playlist_num': 15,
              'spotify_id': '2AFIPUlApcUwGEgOSDwoBz'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'genre': 'classic rock',
              'name': 'See What A Fool I’ve Been - B-Side Version / Remastered 2011',
              'num': 5,
              'num_tracks': 16,
              'year': '1974',
              'playlist_num': 16,
              'spotify_id': '4G4Sf18XkFvNTV5vAxiQyd'}] == songs
    assert (len(songs)) == 16

def test_spotify_playlist_fetch_local_file():
    sp = spotify_auth()
    url = "https://open.spotify.com/playlist/1TWZ36xJ8qkvSeAQQUvU5b?si=ad56b6bb085b4ab9"
    item_type = "playlist"
    songs = fetch_tracks(sp, item_type, url)
    assert [{'album': "Yoshi's Island",
             'artist': 'Koji Kondo',
             'cover': None,
             'genre': '',
             'name': 'Flower Garden',
             'num': 0,
             'num_tracks': None,
             'year': '',
             'playlist_num': 1,
             'spotify_id': None}] == songs
