import sys

from spotify_dl.scaffold import log
from spotify_dl.utils import sanitize


def fetch_tracks(sp, item_type, url):
    """
    Fetches tracks from the provided URL.
    :param sp: Spotify client
    :param item_type: Type of item being requested for: album/playlist/track
    :param url: URL of the item
    :return Dictionary of song and artist
    """
    songs_list = []
    offset = 0

    if item_type == 'playlist':
        while True:
            items = sp.playlist_items(playlist_id=url,

                                      fields='items.track.name,items.track.artists(name, uri),'
                                             'items.track.album(name, release_date, total_tracks, images),'

                                             'items.track.track_number,total, next,offset,'
                                             'items.track.id',
                                      additional_types=['track'], offset=offset)
            total_songs = items.get('total')
            for item in items['items']:
                track_name = item['track']['name']
                track_artist = ", ".join([artist['name'] for artist in item['track']['artists']])
                track_album = item['track']['album']['name']
                track_year = item['track']['album']['release_date'][:4]
                album_total = item['track']['album']['total_tracks']
                track_num = item['track']['track_number']
                spotify_id = item['track']['id']
                if len(item['track']['album']['images']) > 0:
                    cover = item['track']['album']['images'][0]['url']
                else:
                    cover = None
            
                if len(sp.artist(artist_id=item['track']['artists'][0]['uri'])['genres']) > 0:
                    genre = sp.artist(artist_id=item['track']['artists'][0]['uri'])['genres'][0]
                else:
                    genre = ""
                songs_list.append({"name": track_name, "artist": track_artist, "album": track_album, "year": track_year,
                                   "num_tracks": album_total, "num": track_num, "playlist_num": offset + 1,
                                   "cover": cover, "genre": genre, "spotify_id": spotify_id})
                offset += 1

            log.info(f"Fetched {offset}/{total_songs} songs in the playlist")
            if total_songs == offset:
                log.info('All pages fetched, time to leave. Added %s songs in total', offset)
                break

    elif item_type == 'album':
        while True:
            album_info = sp.album(album_id=url)
            items = sp.album_tracks(album_id=url)
            total_songs = items.get('total')
            track_album = album_info['name']
            track_year = album_info['release_date'][:4]
            album_total = album_info['total_tracks']
            if len(album_info['images']) > 0:
                cover = album_info['images'][0]['url']
            else:
                cover = None
            if len(sp.artist(artist_id=album_info['artists'][0]['uri'])['genres']) > 0:
                genre = sp.artist(artist_id=album_info['artists'][0]['uri'])['genres'][0]
            else:
                genre = ""
            for item in items['items']:
                track_name = item['name']
                track_artist = ", ".join([artist['name'] for artist in item['artists']])
                track_num = item['track_number']
                spotify_id = item['id']
                songs_list.append({"name": track_name, "artist": track_artist, "album": track_album, "year": track_year,
                                   "num_tracks": album_total, "num": track_num, "playlist_num": offset + 1,
                                   "cover": cover, "genre": genre, "spotify_id": spotify_id})
                offset += 1

            log.info(f"Fetched {offset}/{total_songs} songs in the album")
            if total_songs == offset:
                log.info('All pages fetched, time to leave. Added %s songs in total', offset)
                break

    elif item_type == 'track':
        items = sp.track(track_id=url)
        track_name = items['name']
        track_artist = ", ".join([artist['name'] for artist in items['artists']])
        track_album = items['album']['name']
        track_year = items['album']['release_date'][:4]
        album_total = items['album']['total_tracks']
        track_num = items['track_number']
        spotify_id = items['id']
        if len(items['album']['images']) > 0:
            cover = items['album']['images'][0]['url']
        else:
            cover = None
        if len(sp.artist(artist_id=items['artists'][0]['uri'])['genres']) > 0:
            genre = sp.artist(artist_id=items['artists'][0]['uri'])['genres'][0]
        else:
            genre = ""
        songs_list.append({"name": track_name, "artist": track_artist, "album": track_album, "year": track_year,
                           "num_tracks": album_total, "num": track_num, "playlist_num": offset + 1,
                           "cover": cover, "genre": genre, "spotify_id": spotify_id})

    return songs_list


def parse_spotify_url(url):
    """
    Parse the provided Spotify playlist URL and determine if it is a playlist, track or album.
    :param url: URL to be parsed

    :return tuple indicating the type and id of the item
    """
    if url.startswith("spotify:"):
        log.error("Spotify URI was provided instead of a playlist/album/track URL.")
        sys.exit(1)
    parsed_url = url.replace("https://open.spotify.com/", "")
    item_type = parsed_url.split("/")[0]
    item_id = parsed_url.split("/")[1]
    return item_type, item_id


def get_item_name(sp, item_type, item_id):
    """
    Fetch the name of the item.
    :param sp: Spotify Client
    :param item_type: Type of the item
    :param item_id: id of the item
    :return String indicating the name of the item
    """
    if item_type == 'playlist':
        name = sp.playlist(playlist_id=item_id, fields='name').get('name')
    elif item_type == 'album':
        name = sp.album(album_id=item_id).get('name')
    elif item_type == 'track':
        name = sp.track(track_id=item_id).get('name')
    return sanitize(name)


def validate_spotify_url(url):
    """
    Validate the URL and determine if the item type is supported.
    :return Boolean indicating whether or not item is supported
    """
    item_type, item_id = parse_spotify_url(url)
    log.debug(f"Got item type {item_type} and item_id {item_id}")
    if item_type not in ['album', 'track', 'playlist']:
        log.info("Only albums/tracks/playlists are supported")
        return False
    if item_id is None:
        log.info("Couldn't get a valid id")
        return False
    return True
