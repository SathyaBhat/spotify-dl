from spotify_dl.models import Song
from peewee import DoesNotExist
from spotify_dl.scaffold import log


def check_if_in_cache(search_term):
    """
    Checks if the specified search term is in the local database cache.
    and returns the video id if it exists.
    :param search_term: String to be searched for in the cache
    :return A tuple with Boolean and video id if it exists
    """
    try:
        song = Song.get(search_term=search_term)
        log.debug(f"Found id {song.video_id} for {search_term} in cache")
        return True, song.video_id
    except DoesNotExist:
        log.debug(f"Couldn't find id for {search_term} in cache")
        return False, None


def save_to_cache(search_term, video_id):
    """
    Saves the search term and video id to the database cache so it can be looked up later.
    :param search_term: Search term to be saved to in the cache
    :param video_id: Video id to be saved to in the cache
    :return Video id saved in the cache
    """
    song_info, saved = Song.get_or_create(search_term=search_term, video_id=video_id)
    log.debug(f"Saved: {saved} video id {song_info.video_id} in cache")
    return song_info.video_id
