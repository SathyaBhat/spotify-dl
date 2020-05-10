from spotify_dl.youtube import fetch_youtube_url, get_youtube_dev_key


def test_fetch_youtube_url(capsys):
    song_link = fetch_youtube_url("Red Hot Chili Peppers - Dani California [Official Music Video]",
                                    get_youtube_dev_key())
    assert song_link == 'https://www.youtube.com/watch?v=Sb5aq5HcS1A'

def test_fetch_youtube_url_wth_scrape(capsys):
    song_link = fetch_youtube_url("Red Hot Chili Peppers - Dani California [Official Music Video]", dev_key=None)
    assert song_link == 'https://www.youtube.com/watch?v=Sb5aq5HcS1A'
