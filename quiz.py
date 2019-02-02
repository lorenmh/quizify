from db import db, Word, Quiz
from glob import glob
from peewee import chunked

db.connect()
db.create_tables([Word, Quiz])

# init
for fname in glob('./words/*.txt'):
    with open(fname, 'r') as f:
        for chunk in chunked([(w,) for w in f.read().splitlines()], 500):
            Word.insert_many(chunk, fields=[Word.name]) \
                .on_conflict_ignore() \
                .execute()
