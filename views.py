from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session

from models import connect_to_db, db


app = Flask(__name__)


QUOTES = ["a i am ", "b i am ", "sam i am "]


@app.route('/')
def index():
    """Show the index."""

    return render_template('index.html')


@app.route('/', methods=['GET'])
def one_random_quote():
    """Return author-choice and single quote as a text string"""
    # "quotes=QUOTE.QUERY.filter". all"
#return a random quote
    return random.choice(QUOTES)
