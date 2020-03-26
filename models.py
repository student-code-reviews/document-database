from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#############################################################################

# class ModelMixin:
#     def save(self):
#         db.session.add(self)
#         db.session.commit()

class Author(db.Model):

    __tablename__ = 'authors'

    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    quotes = db.relationship('Quote', backref='author')
<<<<<<< HEAD
    #sources = db.relationship('Quote', secondary='sources')
=======
>>>>>>> ec52212b70e2697f830d74f530f17c01174749eb

    def __repr__(self):
        return f'<Author {self.id} | {self.name}>'


class Quote(db.Model):

    __tablename__ = 'quotes'

    quote_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    aquote = db.Column(db.String(), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.author_id'))
<<<<<<< HEAD
    #sources = db.relationship('Author', secondary='sources')
=======
>>>>>>> ec52212b70e2697f830d74f530f17c01174749eb

    def __repr__(self):
        return f'<Quote {self.id} | {self.aquote} >'


<<<<<<< HEAD
# class Sources(db.Model):

#     __tablename__ = 'sources'

#     author_id = db.Column(db.Integer, db.ForeignKey('authors.author_id'))
#     quote_id = db.Column(db.Integer, db.ForeignKey('quotes.quote_id'))
#     source = db.Column(db.String())
#     source_id = db.Column(db.Integer, primary_key=True)


=======
>>>>>>> ec52212b70e2697f830d74f530f17c01174749eb
def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///database'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
<<<<<<< HEAD
    from flask import Flask
=======
    from flask import Flask 
>>>>>>> ec52212b70e2697f830d74f530f17c01174749eb
    app = Flask(__name__)

    connect_to_db(app)
    db.drop_all()
    db.create_all()
<<<<<<< HEAD

=======
    
>>>>>>> ec52212b70e2697f830d74f530f17c01174749eb
    print('Connected to database, tables ready.')
