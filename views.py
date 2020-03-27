from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session

from models import Author, Quote, connect_to_db, db

import random
from faker import Faker
from faker.providers import internet

fake = Faker()


app = Flask(__name__)


# QUOTES = ["a i am ", "b i am ", "sam i am]


@app.route('/')
def index():
    """Show the index."""

    return render_template('index.html')


@app.route('/random_quote')
def random_quote():
    """Return a single random quote as a text string"""
    # "quotes=QUOTE.QUERY.filter". all"
#return a random quot
    for quote in range(2):
        print(fake.text())

    # quote = random.choice(fake)
    return render_template('random_quote.html', quote = quote)


@app.route('/authored_quotes')
def authored_quotes():
    """Return authored-choice and single quote as a text string or multiple 
       quotes as"""
    
    return render_template('authored_quote-s.html')


@app.route('/possible_author_identities')
def all_possible_authors():
    """Return list of author possibilities"""
   
    return render_template('possible_author_identities.html')
