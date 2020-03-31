import os
import random

from flask import Flask, render_template, request

from models import Author, Quote


app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secretzzz')


@app.route('/')
def index():
    """Show the index."""

    return render_template('index.html')


@app.route('/random_quote')
def random_quote():
    """Return a single random quote as a text string"""
    # You have this code already.
    choice = random.randrange(1, Quote.count())
    quote = Quote.query.get(choice)
    return render_template('random_quote.html', quote=quote)


@app.route('/authors/search')
def search_by_author():
    """Return authored-choice and single quote as a text string or multiple 
       quotes as"""
    author = request.args.get('author')
    quotes = author.quotes
    return render_template('results.html', quotes=quotes)


@app.route('/authors')
def authors_list():
    """Return list of author possibilities"""
    # TODO: Create a new template and list all the authors on it.
    authors = Author.query.all()
    return render_template('authors_list.html', authors=authors)
