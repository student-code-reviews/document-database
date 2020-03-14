from flask import Flask, render_template
import jinja2


app = Flask(__name__)


app.jinja_env.undefined = jinja2.StrictUndefined


@app.route('/')
def index():
    """Show the index."""

    return render_template('index.html')
