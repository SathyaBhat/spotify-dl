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


def test_download_more_false_skip():
    songs = [{'name': 'Procession - Remastered 2011', 'artist': 'Queen', 'album': 'Queen II (Deluxe Remastered Version)',
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
             'album': 'Queen II (Deluxe Remastered Version)', 'year': '1974', 'num_tracks': 16, 'num': 5}]

    yt.download_songs(songs, download_directory='~/Downloads/queen', format_string='bestaudio/best',
                      skip_mp3=False)

