from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session

from models import Author, Quote, connect_to_db, db

import random


app = Flask(__name__)


QUOTES = ["a i am ", "b i am ", "sam i am "]


@app.route('/')
def index():
    """Show the index."""

    return render_template('index.html')


@app.route('/random_quote')
def random_quote():
    """Return author-choice and single quote as a text string"""
    # "quotes=QUOTE.QUERY.filter". all"
#return a random quot
    quotes = random.choice(QUOTES)
    return render_template('random_quote.html', quotes = quotes)
