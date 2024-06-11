from flask_sqlalchemy import SQLAlchemy
from flaskblog import db, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"User('{self.id}', '{self.title}', '{self.date_posted}')"


def establish_db_connection():
    db_host = "localhost"
    db_port = "5432"
    db_user = "postgres"
    db_pwd = "password"
    db_name = "flaskblog"

    conn = SQLAlchemy(f"postgres://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}")
    return conn
