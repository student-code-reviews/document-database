from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#############################################################################

class Everything(db.Model):

    __tablename__ = 'everything'

    entry_id = db.column(db.Integer, autoincrementing=True, primary_key=True)
    author_id = db.column(db.Integer, nullable=False)
    author_name = db.column(db.String(100), nullable=False)
    quote = db.column(db.String(1000), nullable=False)

    def __repr__(self):
        return f"""<everything entry_id={self.entry_id}
                         author_id={self.author_id}
                         author_name={self.author_name}
                         quote={self.quote}>"""


def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///document-database'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == '__main__'
