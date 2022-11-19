import urllib.request
from os import path
import os
import multiprocessing
import mutagen
import csv
import yt_dlp
from mutagen.easyid3 import EasyID3
from mutagen.id3 import APIC, ID3
from mutagen.mp3 import MP3
from spotify_dl.scaffold import log
from spotify_dl.utils import sanitize
from spotify_dl.constants import DOWNLOAD_LIST


def default_filename(**kwargs):
    """name without number"""
    return sanitize(
        f"{kwargs['artist']} - {kwargs['name']}", "#"
    )  # youtube-dl automatically replaces with #


def playlist_num_filename(**kwargs):
    """name with track number"""
    return f"{kwargs['track_num']} - {default_filename(**kwargs)}"


def write_tracks(tracks_file, song_dict):
    """
    Writes the information of all tracks in the playlist[s] to a text file in csv kind of format
    This includins the name, artist, and spotify URL. Each is delimited by a comma.
    :param tracks_file: name of file towhich the songs are to be written
    :param song_dict: the songs to be written to tracks_file
    """
    track_db = []

    with open(tracks_file, "w+", encoding="utf-8", newline="") as file_out:
        i = 0
        writer = csv.writer(file_out, delimiter=";")
        for url_dict in song_dict["urls"]:
            # for track in url_dict['songs']:
            for track in url_dict["songs"]:
                track_url = track["track_url"]  # here
                track_name = track["name"]
                track_artist = track["artist"]
                track_num = track["num"]
                track_album = track["album"]
                track["save_path"] = url_dict["save_path"]
                track_db.append(track)
                track_index = i
                i += 1
                csv_row = [
                    track_name,
                    track_artist,
                    track_url,
                    str(track_num),
                    track_album,
                    str(track_index),
                ]
                try:
                    writer.writerow(csv_row)
                except UnicodeEncodeError:
                    print(
                        "Track named {track_name} failed due to an encoding error. This is \
                        most likely due to this song having a non-English name."
                    )
    return track_db


def set_tags(temp, filename, kwargs):
    """
     sets song tags after they are downloaded
    :param temp: contains index used to obtain more info about song being editted
    :param filename: location of song whose tags are to be editted
    :param kwargs: a dictionary of extra arguments to be used in tag editing
    """
    song = kwargs["track_db"][int(temp[-1])]
    try:
        song_file = MP3(filename, ID3=EasyID3)
    except mutagen.MutagenError as e:
        log.debug(e)
        print(
            f"Failed to download: {filename}, please ensure YouTubeDL is up-to-date. "
        )

        return
    song_file["date"] = song.get("year")
    if kwargs["keep_playlist_order"]:
        song_file["tracknumber"] = str(song.get("playlist_num"))
    else:
        song_file["tracknumber"] = (
            str(song.get("num")) + "/" + str(song.get("num_tracks"))
        )

    song_file["genre"] = song.get("genre")
    song_file.save()
    song_file = MP3(filename, ID3=ID3)
    cover = song.get("cover")
    if cover is not None:
        if cover.lower().startswith("http"):
            req = urllib.request.Request(cover)
        else:
            raise ValueError from None
        with urllib.request.urlopen(req) as resp:  # nosec
            song_file.tags["APIC"] = APIC(
                encoding=3,
                mime="image/jpeg",
                type=3,
                desc="Cover",
                data=resp.read(),
            )
    song_file.save()


def find_and_download_songs(kwargs):
    """
    function handles actual download of the songs
    the youtube_search lib is used to search for songs and get best url
    :param kwargs: dictionary of key value arguments to be used in download
    """
    sponsorblock_postprocessor = []
    reference_file = kwargs["reference_file"]
    with open(reference_file, "r", encoding="utf-8") as file:
        for line in file:
            temp = line.split(";")
            name, artist, album, i = (
                temp[0],
                temp[1],
                temp[4],
                int(temp[-1].replace("\n", "")),
            )

            query = f"{artist} - {name} Lyrics".replace(":", "").replace('"', "")
            print(f"Initiating download for {query}.")

            file_name = kwargs["file_name_f"](
                name=name, artist=artist, track_num=kwargs["track_db"][i].get("num")
            )

            if kwargs["use_sponsorblock"][0].lower() == "y":

                sponsorblock_postprocessor = [
                    {
                        "key": "SponsorBlock",
                        "categories": ["skip_non_music_sections"],
                    },
                    {
                        "key": "ModifyChapters",
                        "remove_sponsor_segments": ["music_offtopic"],
                        "force_keyframes": True,
                    },
                ]

            file_path = path.join(kwargs["track_db"][i]["save_path"], file_name)

            mp3filename = f"{file_path}.mp3"
            mp3file_path = path.join(mp3filename)

            if kwargs["no_overwrites"] and not kwargs["skip_mp3"] and path.exists(mp3file_path):
                print(f'File {mp3filename} already exists, we do not overwrite it ')
                continue

            outtmpl = f"{file_path}.%(ext)s"
            ydl_opts = {
                "proxy": kwargs.get('proxy'),
                "default_search": "ytsearch",
                "format": "bestaudio/best",
                "outtmpl": outtmpl,
                "postprocessors": sponsorblock_postprocessor,
                "noplaylist": True,
                "no_color": False,
                "postprocessor_args": [
                    "-metadata",
                    "title=" + name,
                    "-metadata",
                    "artist=" + artist,
                    "-metadata",
                    "album=" + album,
                ],
            }
            if not kwargs["skip_mp3"]:
                mp3_postprocess_opts = {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
                ydl_opts["postprocessors"].append(mp3_postprocess_opts.copy())
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                try:
                    ydl.download([query])
                except Exception as e:  # skipcq: PYL-W0703
                    log.debug(e)
                    print(f"Failed to download {name}, make sure yt_dlp is up to date")
            if not kwargs["skip_mp3"]:
                set_tags(temp, mp3filename, kwargs)


def multicore_find_and_download_songs(kwargs):
    """
    function handles divinding songs to be downloaded among the specified number of CPU's
    extra songs are shared among the CPU's
    each cpu then handles its own batch through the multihandler fn
    """
    reference_file = kwargs["reference_file"]
    lines = []
    with open(reference_file, "r", encoding="utf-8") as file:
        for line in file:
            lines.append(line)
    cpu_count = kwargs["multi_core"]
    number_of_songs = len(lines)
    songs_per_cpu = number_of_songs // cpu_count
    extra_songs = number_of_songs % cpu_count

    cpu_count_list = []
    for cpu in range(cpu_count):
        songs = songs_per_cpu
        if cpu < extra_songs:
            songs = songs + 1
        cpu_count_list.append(songs)

    index = 0
    file_segments = []
    for cpu in cpu_count_list:
        right = cpu + index
        segment = lines[index:right]
        index = index + cpu
        file_segments.append(segment)

    processes = []
    segment_index = 0
    for segment in file_segments:
        p = multiprocessing.Process(
            target=multicore_handler, args=(segment_index, segment, kwargs.copy())
        )
        processes.append(p)
        segment_index += 1

    for p in processes:
        p.start()
    for p in processes:
        p.join()


def multicore_handler(segment_index, segment, kwargs):
    """
    function to handle each unique processor spawned download job
    :param segment_index: to be used for naming the reference file to be used for processor's download batch
    :param segment: list of songs to be downloaded using spawning processor
    """
    reference_filename = f"{segment_index}.txt"
    with open(reference_filename, "w+", encoding="utf-8") as file_out:
        for line in segment:
            file_out.write(line)

    kwargs["reference_file"] = reference_filename
    find_and_download_songs(kwargs)

    if os.path.exists(reference_filename):
        os.remove(reference_filename)


def download_songs(**kwargs):
    """
    Downloads songs from the YouTube URL passed to either current directory or download_directory, as it is passed.  [made small typo change]
    :param kwargs: keyword arguments to be passed on between functions when downloading
    """
    for url in kwargs["songs"]["urls"]:
        log.debug("Downloading to %s", url["save_path"])
    reference_file = DOWNLOAD_LIST
    track_db = write_tracks(reference_file, kwargs["songs"])
    os.rename(reference_file, kwargs["output_dir"] + "/" + reference_file)
    reference_file = str(kwargs["output_dir"]) + "/" + reference_file
    kwargs["reference_file"] = reference_file
    kwargs["track_db"] = track_db
    if kwargs["multi_core"] > 1:
        multicore_find_and_download_songs(kwargs)
    else:
        find_and_download_songs(kwargs)
    os.remove(reference_file)
