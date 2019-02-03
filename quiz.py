from db import db, Word, Quiz
from glob import glob
from peewee import chunked, fn, Expression

from wiktionaryparser import WiktionaryParser
parser = WiktionaryParser()

db.connect()
db.create_tables([Word, Quiz])

RANDOM_FACTOR = 100
WRONG_FACTOR = 10
MOST_RECENT = 4


def mod(lhs, rhs):
    return Expression(lhs, '%', rhs)


# init
for fname in glob('./words/*.txt'):
    with open(fname, 'r') as f:
        for chunk in chunked([(w,) for w in f.read().splitlines()], 500):
            Word.insert_many(chunk, fields=[Word.name]) \
                .on_conflict_ignore() \
                .execute()

def get_random():
    random_weight = Word.weight * fn.Abs(mod(fn.Random(), RANDOM_FACTOR))
    return Word.select() \
               .order_by(random_weight.desc()) \
               .get()

# TODO: implement
def select_random_weighted():
    '''
    ((ratio_quizes_wrong * wrong_factor) + weight) * abs(random % random_factor)
    '''
    pass
