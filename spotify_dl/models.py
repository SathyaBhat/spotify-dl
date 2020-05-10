from peewee import SqliteDatabase
from peewee import Model, TextField
from os import path

db = SqliteDatabase(path.expanduser('~/.songs.db'))


class Song(Model):
    search_term = TextField()
    video_id = TextField()

    class Meta:
        database = db
