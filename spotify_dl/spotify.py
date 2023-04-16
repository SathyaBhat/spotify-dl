import sys
from spotify_dl.scaffold import log
from spotify_dl.utils import sanitize
from rich.progress import Progress


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
    songs_fetched = 0

    if item_type == "playlist":
        with Progress() as progress:
            songs_task = progress.add_task(description="Fetching songs from playlist..")
            while True:
                items = sp.playlist_items(
                    playlist_id=url,
                    fields="items.track.name,items.track.artists(name, uri),"
                    "items.track.album(name, release_date, total_tracks, images),"
                    "items.track.track_number,total, next,offset,"
                    "items.track.id",
                    additional_types=["track"],
                    offset=offset,
                )
                total_songs = items.get("total")
                track_info_task = progress.add_task(
                    description="Fetching track info", total=len(items["items"])
                )
                for item in items["items"]:
                    track_info = item.get("track")
                    # If the user has a podcast in their playlist, there will be no track
                    # Without this conditional, the program will fail later on when the metadata is fetched
                    if track_info is None:
                        offset += 1
                        continue
                    track_album_info = track_info.get("album")
                    track_num = track_info.get("track_number")
                    spotify_id = track_info.get("id")
                    track_name = track_info.get("name")
                    track_artist = ",".join(
                        [artist["name"] for artist in track_info.get("artists")]
                    )
                    if track_album_info:
                        track_album = track_album_info.get("name")
                        track_year = (
                            track_album_info.get("release_date")[:4]
                            if track_album_info.get("release_date")
                            else ""
                        )
                        album_total = track_album_info.get("total_tracks")
                    if len(item["track"]["album"]["images"]) > 0:
                        cover = item["track"]["album"]["images"][0]["url"]
                    else:
                        cover = None

                    artists = track_info.get("artists")
                    main_artist_id = (
                        artists[0].get("uri", None) if len(artists) > 0 else None
                    )
                    genres = (
                        sp.artist(artist_id=main_artist_id).get("genres", [])
                        if main_artist_id
                        else []
                    )
                    if len(genres) > 0:
                        genre = genres[0]
                    else:
                        genre = ""
                    songs_list.append(
                        {
                            "name": track_name,
                            "artist": track_artist,
                            "album": track_album,
                            "year": track_year,
                            "num_tracks": album_total,
                            "num": track_num,
                            "playlist_num": offset + 1,
                            "cover": cover,
                            "genre": genre,
                            "spotify_id": spotify_id,
                            "track_url": None,
                        }
                    )
                    offset += 1
                    songs_fetched += 1
                    progress.update(
                        task_id=track_info_task,
                        description=f"Fetching track info for \n{track_name}",
                        advance=1,
                    )

                progress.update(
                    task_id=songs_task,
                    description=f"Fetched {songs_fetched} of {total_songs} songs from the playlist",
                    advance=100,
                    total=total_songs,
                )
                if total_songs == offset:
                    break

    elif item_type == "album":
        with Progress() as progress:
            album_songs_task = progress.add_task(
                description="Fetching songs from the album.."
            )
            while True:
                album_info = sp.album(album_id=url)
                items = sp.album_tracks(album_id=url, offset=offset)
                total_songs = items.get("total")
                track_album = album_info.get("name")
                track_year = (
                    album_info.get("release_date")[:4]
                    if album_info.get("release_date")
                    else ""
                )
                album_total = album_info.get("total_tracks")
                if len(album_info["images"]) > 0:
                    cover = album_info["images"][0]["url"]
                else:
                    cover = None
                if (
                    len(sp.artist(artist_id=album_info["artists"][0]["uri"])["genres"])
                    > 0
                ):
                    genre = sp.artist(artist_id=album_info["artists"][0]["uri"])[
                        "genres"
                    ][0]
                else:
                    genre = ""
                for item in items["items"]:
                    track_name = item.get("name")
                    track_artist = ", ".join(
                        [artist["name"] for artist in item["artists"]]
                    )
                    track_num = item["track_number"]
                    spotify_id = item.get("id")
                    songs_list.append(
                        {
                            "name": track_name,
                            "artist": track_artist,
                            "album": track_album,
                            "year": track_year,
                            "num_tracks": album_total,
                            "num": track_num,
                            "track_url": None,
                            "playlist_num": offset + 1,
                            "cover": cover,
                            "genre": genre,
                            "spotify_id": spotify_id,
                        }
                    )
                    offset += 1

                progress.update(
                    task_id=album_songs_task,
                    description=f"Fetched {offset} of {album_total} songs from the album {track_album}",
                    advance=offset,
                    total=album_total,
                )
                if album_total == offset:
                    break

    elif item_type == "track":
        items = sp.track(track_id=url)
        track_name = items.get("name")
        album_info = items.get("album")
        track_artist = ", ".join([artist["name"] for artist in items["artists"]])
        if album_info:
            track_album = album_info.get("name")
            track_year = (
                album_info.get("release_date")[:4]
                if album_info.get("release_date")
                else ""
            )
            album_total = album_info.get("total_tracks")
        track_num = items["track_number"]
        spotify_id = items["id"]
        if len(items["album"]["images"]) > 0:
            cover = items["album"]["images"][0]["url"]
        else:
            cover = None
        if len(sp.artist(artist_id=items["artists"][0]["uri"])["genres"]) > 0:
            genre = sp.artist(artist_id=items["artists"][0]["uri"])["genres"][0]
        else:
            genre = ""
        songs_list.append(
            {
                "name": track_name,
                "artist": track_artist,
                "album": track_album,
                "year": track_year,
                "num_tracks": album_total,
                "num": track_num,
                "playlist_num": offset + 1,
                "cover": cover,
                "genre": genre,
                "track_url": None,
                "spotify_id": spotify_id,
            }
        )

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
    parsed_url = url.replace("https://open.spotify.com/", "").split("?")[0]
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
    if item_type == "playlist":
        name = sp.playlist(playlist_id=item_id, fields="name").get("name")
    elif item_type == "album":
        name = sp.album(album_id=item_id).get("name")
    elif item_type == "track":
        name = sp.track(track_id=item_id).get("name")
    return sanitize(name)


def validate_spotify_urls(urls):
    """
    Validate the URLs and determine if the item types they have are supported
    : return a list of valid urls
    """
    valid_urls = []
    for url in urls:
        item_type, item_id = parse_spotify_url(url)
        log.debug("Got item_type %s and item_id %s", item_type, item_id)
        if item_type not in ["album", "track", "playlist"]:
            log.info("Only albums/tracks/playlists are supported and not %s", item_type)
            continue
        if item_id is None:
            log.info("Couln't get valid item_id for %s", url)
        else:
            valid_urls.append(url)
    return valid_urls
