from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "04f27db8cc9e9ce6eb47956f8446e5b2"
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://postgres:password@localhost:5432/flaskblog"
)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"

from flaskblog.Users.routes import users
from flaskblog.Main.routes import main
from flaskblog.Post.routes import posts

app.register_blueprint(users)
app.register_blueprint(main)
app.register_blueprint(posts)
