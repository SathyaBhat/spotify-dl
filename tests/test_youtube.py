from spotify_dl import youtube as yt


def test_download_one_false_skip():
    songs = [ {'name': 'Simple Song', 'artist': 'The Shins', 'album': 'Simple Song', 'year': '2012',
               'num_tracks': 1,
            'num': 1}]
    yt.download_songs(songs, download_directory='~/Downloads', format_string='best',
                      skip_mp3=False)


def test_download_one_true_skip():
    songs = [
        {'name': 'Simple Song', 'artist': 'The Shins', 'album': 'Simple Song', 'year': '2012', 'num_tracks': 1,
         'num': 1}]
    yt.download_songs(songs, download_directory='~/Downloads', format_string='bestvideo',
                      skip_mp3=True)


