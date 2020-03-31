from models import *
from faker import Faker
from faker.providers import lorem
fake = Faker()

fake.texts(nb_texts=3, max_nb_chars=200, ext_word_list=None)

def seed():

    aquote = Quote(aquote=faker.text())

    for q in range(1):
        print(quote_id=fake.text())

        aquote.quotes.append(quote)
        db.session.add(quote)

        db.session.add(aquote)
        db.session.commit()
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