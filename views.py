from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session

from models import connect_to_db, db, Author, Quote


# import os
import random
# import seed
from faker import Faker

from faker.providers import lorem

fake = Faker()


app = Flask(__name__)
# app.secret_key = os.getenv('SECRET_KEY', 'secretzzz')


# QUOTES = ["a i am ", "b i am ", "sam i am]


@app.route('/')
def index():
    """Show the index."""

    return render_template('index.html')


@app.route('/random_quote')
def random_quote():
    """Return a single random quote as a text string"""
    # "quotes=QUOTE.QUERY.filter". all"
    # quote = random.choice(fake)
    # quotes = Quote.query.all()
    for quote in range(1):
        print(fake.text())
        
    return render_template('random_quote.html', quote = quote)


@app.route('/new_random_quote')
def new_random_quote():

    return render_template('quotes/new_random_quote_form.html')


@app.route('/authored_quotes')
def authored_quotes():
    """Return authored-choice and single quote as a text string or multiple 
       quotes as"""
    return render_template('authored_quote-s.html')


@app.route('/possible_author_identities')
def all_possible_authors():
    """Return list of author possibilities"""
    return render_template('possible_author_identities.html')


    # if __name__ == '__main__':
    #     app.run(debug=True, host="0.0.0.0")

    #     connect_to_db(app)

    #     app.run()

