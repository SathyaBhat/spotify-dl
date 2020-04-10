from spotify_dl.youtube import fetch_youtube_url


def test_fetch_youtube_url(capsys):
    # song_link = fetch_youtube_url("Red Hot Chili Peppers - Dani California [Official Music Video]")
    # assert song_link is None
    # captured = capsys.readouterr()
    # assert "keyInvalid" in captured.out
    song_link = fetch_youtube_url("Red Hot Chili Peppers - Dani California [Official Music Video]")
    assert song_link == 'https://www.youtube.com/watch?v=Sb5aq5HcS1A'
