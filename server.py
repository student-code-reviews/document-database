 # from flask import Flask, render_template
#from model import connect_to_db
from views import app


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
