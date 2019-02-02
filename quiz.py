from db import db, Word, Quiz
from glob import glob
from peewee import chunked

db.connect()
db.create_tables([Word, Quiz])

RANDOM_FACTOR = 100
WRONG_FACTOR = 10
MOST_RECENT = 4

# init
for fname in glob('./words/*.txt'):
    with open(fname, 'r') as f:
        for chunk in chunked([(w,) for w in f.read().splitlines()], 500):
            Word.insert_many(chunk, fields=[Word.name]) \
                .on_conflict_ignore() \
                .execute()

'''
(RatioWrong * WRONG_FACTOR + weight) * ABS(RANDOM() % 100)
'''
next_quiz_word = 'some crazy query'
