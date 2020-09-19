from peewee import SqliteDatabase
from peewee import Model, TextField
from os import path
from pathlib import Path
from spotify_dl.constants import SAVE_PATH

Path(path.expanduser(SAVE_PATH)).mkdir(exist_ok=True)
db = SqliteDatabase(path.expanduser(f"{SAVE_PATH}/songs.db"))


class Song(Model):
    search_term = TextField()
    video_id = TextField()

    class Meta:
        database = db
