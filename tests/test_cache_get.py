from spotify_dl.cache import check_if_in_cache, save_to_cache
from spotify_dl.models import db, Song

search_term_wrong = 'bleh'
search_term = "Red Hot Chili Peppers - Dani California [Official Music Video]"

video_id = "Sb5aq5HcS1A"
db.connect()
db.create_tables([Song])

def test_check_for_cache_miss():
    exists, song_info = check_if_in_cache(search_term=search_term_wrong)
    assert exists is False
    assert song_info is None

def test_check_for_cache_hit():
    _ = save_to_cache(search_term=search_term, video_id='Sb5aq5HcS1A')
    exists, cache_video_id = check_if_in_cache(search_term=search_term)
    assert exists is True
    assert cache_video_id == video_id