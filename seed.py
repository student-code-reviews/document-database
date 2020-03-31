from models import *
from faker import Faker
from faker.providers import lorem
fake = Faker()

fake.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None)

QUOTES = {'Author': 'Quote'}


def seed():

    for a, q in QUOTES.items():
        author = Author(name=a)
        author.save()

        quote = Quote(text=q, author_id=author.author_id)
        quote.save()

    print('Seeding successful.')


if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    db.reflect()
    db.drop_all()
    db.create_all()

    seed()
    print('Data ready. Time to code!')
