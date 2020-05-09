from peewee import SqliteDatabase
from peewee import Model, TextField

db = SqliteDatabase('.songs.db')


class Song(Model):
    search_term = TextField()
    video_id = TextField()

    class Meta:
        database = db