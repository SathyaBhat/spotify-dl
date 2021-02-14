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
    yt.download_songs(songs, download_directory='~/Downloads', format_string='best',
                      skip_mp3=False)

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
