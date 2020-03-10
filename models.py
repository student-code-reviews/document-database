from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#############################################################################

class User_main_info(db.Model):

    __tablename__ = 'user_main_info'

    user_id = db.column(db.Integer, nullable=False, primary_key=True)
    main_folder_id = db.column(db.Integer, nullable=False)
    fname = db.column(db.String(50), nullable=False)
    lname = db.column(db.String(50), nullable=False)
    email = db.column(db.String, unique=True)
    username = db.Column(db.String(75), nullable=False)


    def __repr__(self):
        return f"""<User_main_info user_id={self.user_id}
                         main_folder_id={self.main_folder_id}
                         fname={self.fname}
                         lname={self.lname}
                         email={self.email}
                         username={self.username}>"""


class Authentication(db.Model):

    __tablename__ = 'authentication'

    user_id = db.column(db.Integer, nullable=False, Foreign_key=True)
    username = db.column(db.String(75), nullable=False)
    password = db.column(db.String(36), nullable=False)
    password_hint = db.column(db.String(200), nullable=True)

    def __repr__(self):
        return f"""<Authentiction user_id={self.user_id}
                                  username={self.username}
                                  password={self.password}
                                  password_hint{self.password_hint}>"""


class Docs(db.Model):

    __tablename__ = 'docs'

    main_folder_id = db.column(db.Integer, nullable=False, Foreign_key=True)
    folder_id = db.column(db.Integer, nullable-False)
    doc_id = db.column(db.Integer, nullable=False)

    def __repr__(self):
        return f"""<Docs main_folder_id={self.main_folder_id}
                         folder_id={self.folder_id}
                         doc_id={self.doc_id}>"""


def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///herotome'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    db.create_all()

    print('Connected to database, tables ready.')
