from gevent import monkey; monkey.patch_all()
from peewee import SqliteDatabase, Model, ForeignKeyField, IntegerField, \
                   CharField, TextField, DateTimeField, BooleanField

from datetime import datetime

db = SqliteDatabase('quiz.db')


class Base(Model):
    class Meta:
        database = db


class Word(Base):
    name = CharField(max_length=255, unique=True)
    definition = TextField(null=True)
    etymology = TextField(null=True)
    weight = IntegerField(default=1)


class Quiz(Base):
    word = ForeignKeyField(Word, backref='quizes', on_delete='CASCADE')
    dt = DateTimeField(default=datetime.now)
    attempt = TextField(null=True)
    is_correct = BooleanField()
