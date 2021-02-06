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
    assert {'album': 'Hell Freezes Over (Remaster 2018)',
     'artist': 'Eagles',
     'cover': 'https://i.scdn.co/image/ab67616d0000b27396d28597a5ae44ab66552183',
     'name': 'Hotel California - Live On MTV, 1994',
     'num': 6,
     'num_tracks': 15,
     'year': '1994'} == songs[0]


def test_spotify_playlist_fetch_more():
    sp = spotify_auth()
    url = "https://open.spotify.com/playlist/3cEYpjA9oz9GiPac4AsH4n"
    item_type = "playlist"
    songs = fetch_tracks(sp, item_type, url)
    assert  {'album': 'Progressive Psy Trance Picks Vol.8',
             'artist': 'Odiseo',
             'cover': 'https://i.scdn.co/image/ab67616d0000b273ce6d0eef0c1ce77e5f95bbbc',
             'name': 'Api',
             'num': 10,
             'num_tracks': 20,
             'year': '2012'} == songs[0]
    assert {'album': 'Wellness & Dreaming Source',
             'artist': 'Vlasta Marek',
             'cover': 'https://i.scdn.co/image/ab67616d0000b273aa2ff29970d9a63a49dfaeb2',
             'name': 'Is',
             'num': 21,
             'num_tracks': 25,
             'year': '2015'} \
           == songs[1]
    assert {'album': 'This Is Happening',
             'artist': 'LCD Soundsystem',
             'cover': 'https://i.scdn.co/image/ab67616d0000b273ee0d0dce888c6c8a70db6e8b',
             'name': 'All I Want',
             'num': 4,
             'num_tracks': 9,
             'year': '2010'} \
           == songs[2]
    assert {'album': 'Glenn Horiuchi Trio / Gelenn Horiuchi Quartet: Mercy / Jump Start / '
          'Endpoints / Curl Out / Earthworks / Mind Probe / Null Set / Another '
          'Space (A)',
         'artist': 'Glenn Horiuchi Trio',
         'cover': 'https://i.scdn.co/image/ab67616d0000b2738b7447ac3daa1da18811cf7b',
         'name': 'Endpoints',
         'num': 2,
         'num_tracks': 8,
         'year': '2011'} \
           == songs[3]
    assert {'album': 'All The Best (Spanish Version)',
             'artist': 'Zucchero',
             'cover': 'https://i.scdn.co/image/ab67616d0000b27304e57d181ff062f8339d6c71',
             'name': 'You Are So Beautiful',
             'num': 18,
             'num_tracks': 18,
             'year': '2007'} \
           == songs[4]


def test_spotify_track_fetch_one():
    sp = spotify_auth()
    url = "https://open.spotify.com/track/7HW5WIw7ZgZORCzUxv5gW5?si=iJAXeqvJQW2BY04eVBgpGw"
    item_type = "track"
    songs = fetch_tracks(sp, item_type, url)
    assert {'album': 'Rock Of The Westies',
             'artist': 'Elton John, Kiki Dee',
             'cover': 'https://i.scdn.co/image/ab67616d0000b27342a15a4fe15a8a88ab728d5b',
             'name': "Don't Go Breaking My Heart",
             'num': 10,
             'num_tracks': 10,
             'year': '1975'} == songs[0]


def test_spotify_album_fetch_one():
    sp = spotify_auth()
    url = "https://open.spotify.com/album/1IVEQdX6Y37za9PMB0afPX?si=Hz8CMaYpTx2O0PeuDglKaA"
    item_type = "album"
    songs = fetch_tracks(sp, item_type, url)
    assert {'album': 'Simple Song',
             'artist': 'The Shins',
             'cover': 'https://i.scdn.co/image/ab67616d0000b2737f6f8d24f3bba324727d6021',
             'name': 'Simple Song',
             'num': 1,
             'num_tracks': 1,
             'year': '2012'} == songs[0]


def test_spotify_album_fetch_more():
    sp = spotify_auth()
    url = "https://open.spotify.com/album/2RKEso6nin3nhRyAd36Omv?si=KEBaFQxYR9-nRJLarH2QNQ"
    item_type = "album"
    songs = fetch_tracks(sp, item_type, url)
    assert [{'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'name': 'Procession - Remastered 2011',
              'num': 1,
              'num_tracks': 16,
              'year': '1974'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'name': 'Father To Son - Remastered 2011',
              'num': 2,
              'num_tracks': 16,
              'year': '1974'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'name': 'White Queen (As It Began) - Remastered 2011',
              'num': 3,
              'num_tracks': 16,
              'year': '1974'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'name': 'Some Day One Day - Remastered 2011',
              'num': 4,
              'num_tracks': 16,
              'year': '1974'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'name': 'The Loser In The End - Remastered 2011',
              'num': 5,
              'num_tracks': 16,
              'year': '1974'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'name': 'Ogre Battle - Remastered 2011',
              'num': 6,
              'num_tracks': 16,
              'year': '1974'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'name': "The Fairy Feller's Master-Stroke - Remastered 2011",
              'num': 7,
              'num_tracks': 16,
              'year': '1974'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'name': 'Nevermore - Remastered 2011',
              'num': 8,
              'num_tracks': 16,
              'year': '1974'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'name': 'The March Of The Black Queen - Remastered 2011',
              'num': 9,
              'num_tracks': 16,
              'year': '1974'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'name': 'Funny How Love Is - Remastered 2011',
              'num': 10,
              'num_tracks': 16,
              'year': '1974'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'name': 'Seven Seas Of Rhye - Remastered 2011',
              'num': 11,
              'num_tracks': 16,
              'year': '1974'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'name': "See What A Fool I've Been - Live BBC Session, London / July 1973 / "
                      '2011 Remix',
              'num': 1,
              'num_tracks': 16,
              'year': '1974'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'name': 'White Queen (As It Began) - Live At Hammersmith Odeon, London / '
                      'December 1975',
              'num': 2,
              'num_tracks': 16,
              'year': '1974'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'name': 'Seven Seas Of Rhye - Instrumental Mix 2011',
              'num': 3,
              'num_tracks': 16,
              'year': '1974'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'name': 'Nevermore - Live BBC Session, London / April 1974',
              'num': 4,
              'num_tracks': 16,
              'year': '1974'},
             {'album': 'Queen II (Deluxe Remastered Version)',
              'artist': 'Queen',
              'cover': 'https://i.scdn.co/image/ab67616d0000b273dcf482c792ef848d7a994fd5',
              'name': 'See What A Fool I’ve Been - B-Side Version / Remastered 2011',
              'num': 5,
              'num_tracks': 16,
              'year': '1974'}] == songs
    assert (len(songs)) == 16
