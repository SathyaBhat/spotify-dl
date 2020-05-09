from json import dump, load
from spotify_dl.models import db, Song
from peewee import DoesNotExist

def check_if_in_cache(search_term):
    try:
        song = Song.get(search_term=search_term)
        return True, song.video_id
    except DoesNotExist:
        return False, None

def save_to_cache(search_term, video_id):
    song_info, _ = Song.get_or_create(search_term=search_term, video_id=video_id)
    return song_info.video_id