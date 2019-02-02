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


class Quiz(Base):
    dt = DateTimeField(default=datetime.now)
    word = ForeignKeyField(Word, backref='quizes')
    is_correct = BooleanField()
    confidence = IntegerField()
