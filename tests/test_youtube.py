import os
import urllib
import urllib.request

from mutagen.easyid3 import EasyID3
from mutagen.id3 import APIC, ID3
from mutagen.mp3 import MP3

from spotify_dl import youtube as yt


def test_download_one_false_skip():
    songs = [{'album': 'Hell Freezes Over (Remaster 2018)',
              'artist': 'Eagles',
              'cover': 'https://i.scdn.co/image/ab67616d0000b27396d28597a5ae44ab66552183',
              'genre': 'album rock',
              'name': 'Hotel California - Live On MTV, 1994',
              'num': 6,
              'num_tracks': 15,
              'year': '1994'}]
    yt.download_songs(songs, download_directory=os.path.dirname(os.path.realpath(__file__)),
                      format_string='best',
                      skip_mp3=False)
    music = MP3("tests/Eagles - Hotel California - Live On MTV, 1994.mp3", ID3=EasyID3)
    tags = ID3("tests/Eagles - Hotel California - Live On MTV, 1994.mp3")
    assert (music['artist'][0] == 'Eagles')
    assert (music['album'][0] == 'Hell Freezes Over (Remaster 2018)')
    assert (music['genre'][0] == 'album rock')
    assert (tags.getall("APIC")[0].data == APIC(encoding=3,
                                                mime='image/jpeg',
                                                type=3, desc=u'Cover',
                                                data=urllib.request.urlopen(songs[0].get('cover')).read()
                                                ))

def test_download_one_true_skip():
    songs = [
        {'album': 'Hell Freezes Over (Remaster 2018)',
         'artist': 'Eagles',
         'cover': 'https://i.scdn.co/image/ab67616d0000b27396d28597a5ae44ab66552183',
         'genre': 'album rock',
         'name': 'Hotel California - Live On MTV, 1994',
         'num': 6,
         'num_tracks': 15,
         'year': '1994'}]
    yt.download_songs(songs, download_directory='~/Downloads', format_string='best',
                      skip_mp3=False)

def test_download_cover_none():
    songs = [
        {'album': 'Queen II (Deluxe Remastered Version)',
         'artist': 'Queen',
         'cover': None,
         'genre': 'classic rock',
         'name': "The Fairy Feller's Master-Stroke - Remastered 2011",
         'num': 7,
         'num_tracks': 16,
         'year': '1974'}]
    yt.download_songs(songs, download_directory=os.path.dirname(os.path.realpath(__file__)),
                      format_string='best',
                      skip_mp3=False)
    music = MP3("tests/Queen - The Fairy Feller's Master-Stroke - Remastered 2011.mp3", ID3=EasyID3)
    tags = ID3("tests/Queen - The Fairy Feller's Master-Stroke - Remastered 2011.mp3")
    assert (music['artist'][0] == 'Queen')
    assert (music['album'][0] == 'Queen II (Deluxe Remastered Version)')
    assert (music['genre'][0] == 'classic rock')
    assert (len(tags.getall("APIC")) == 0)