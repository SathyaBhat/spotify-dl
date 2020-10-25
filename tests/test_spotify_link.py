from spotify_dl.spotify import parse_spotify_url

def test_parse_spotify_url():
    album_url = "https://open.spotify.com/album/aabbccddee"
    playlist_url = "https://open.spotify.com/playlist/aabbccddee"
    track_url = "https://open.spotify.com/track/aabbccddee"

    type, id = parse_spotify_url(album_url)
    assert type == 'album'
    assert id == 'aabbccddee'

    type, id = parse_spotify_url(playlist_url)
    assert type == 'playlist'
    assert id == 'aabbccddee'

    type, id = parse_spotify_url(track_url)
    assert type == 'track'
    assert id == 'aabbccddee'