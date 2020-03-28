from spotify_dl.youtube import fetch_youtube_url, get_youtube_dev_key


def test_fetch_youtube_url(capsys):
    song_link = fetch_youtube_url("Red Hot Chili Peppers - Dani California [Official Music Video]",
                                    "12354")
    assert song_link is None
    captured = capsys.readouterr()
    assert "keyInvalid" in captured.out
    song_link = fetch_youtube_url("Red Hot Chili Peppers - Dani California [Official Music Video]",
                                    get_youtube_dev_key())
    assert song_link == 'https://www.youtube.com/watch?v=Sb5aq5HcS1A'
