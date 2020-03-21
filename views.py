from flask import Flask, render_template
# from model import Author, Quote, Source
import jinja2
import random


app = Flask(__name__)


app.jinja_env.undefined = jinja2.StrictUndefined


QUOTES = ["a i am ", "b i am ", "sam i am "]


@app.route('/')
def index():
    """Show the index."""

    return render_template('index.html')


@app.route('/author_choice', methods=['POST'])
def one_random_quote():
    """Return author-choice and single quote as a text string"""
    # "quotes=QUOTE.QUERY.filter". all"
#return a random quote
    return random.choice(QUOTES)
