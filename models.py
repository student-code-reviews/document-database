from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#############################################################################

# class ModelMixin:
#     def save(self):
#         db.session.add(self)
#         db.session.commit()

sources_table = db.Table('sources',
                         db.Column('author_id', db.Integer,
                                   db.ForeignKey('authors.id')),
                         db.Column('quote_id', db.Integer,
                                   db.ForeignKey('quotes.id')),
                         db.Column('source', db.String(200)))


class Author(db.Model):

    __tablename__ = 'authors'

    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String(100), nullable=False)
    sources = db.relationship('Quote', secondary='sources')

    def __repr__(self):
        return f'<Author {self.id} | {self.name}>'


class Quote(db.Model):

    __tablename__ = 'quotes'

    id = db.column(db.Integer, autoincrementing=True, primary_key=True)
    aquote = db.column(db.String(1000), nullable=False)
    sources = db.relationship('Author', secondary='sources')

    def __repr__(self):
        return f'<Quote {self.id} | {self.aquote} >'


def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///database'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    with app.app_context():
        db.create_all()


if __name__ == '__main__'


print('Connected to database, tables ready.')
