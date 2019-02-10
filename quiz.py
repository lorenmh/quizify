from gevent import monkey; monkey.patch_all()
from gevent.pool import Pool

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

POOL_SZ = 16


def mod(lhs, rhs):
    return Expression(lhs, '%', rhs)

# init
for fname in glob('./words/*.txt'):
    with open(fname, 'r') as f:
        for chunk in chunked([(w,) for w in f.read().splitlines()], 500):
            Word.insert_many(chunk, fields=[Word.name]) \
                .on_conflict_ignore() \
                .execute()


def update_definition(word):
    print('fetching "{}"'.format(word.name))
    try:
        d = parser.fetch(word.name, 'english')[0]
        definition_lines = d['definitions'][0]['text']
        definition = '\n\t'.join(definition_lines)
        etymology = d.get('etymology')
        word.definition = definition
        word.etymology = etymology
    except:
        pass
    return word

pool = Pool(POOL_SZ)
undefined_words = Word.select().where(Word.definition == None)
updated_words = pool.map(update_definition, undefined_words)
[word.save() for word in updated_words]

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
