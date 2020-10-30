from spotify_dl.spotify import parse_spotify_url

def test_parse_spotify_url():
    album_url = "https://open.spotify.com/album/aabbccddee"
    playlist_url = "https://open.spotify.com/playlist/aabbccddee"
    track_url = "https://open.spotify.com/track/aabbccddee"

    item_type, item_id = parse_spotify_url(album_url)
    assert item_type == 'album'
    assert item_id == 'aabbccddee'

    item_type, item_id = parse_spotify_url(playlist_url)
    assert item_type == 'playlist'
    assert item_id == 'aabbccddee'

    item_type, item_id = parse_spotify_url(track_url)
    assert item_type == 'track'
    assert item_id == 'aabbccddee'