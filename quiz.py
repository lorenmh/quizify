from db import db, Word, Quiz

db.connect()
db.create_tables([Word, Quiz])
