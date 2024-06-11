from flask import Blueprint, render_template
from flaskblog.db_connect import Post

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home():
    posts = Post.query.all()
    return render_template("home.html", posts=posts, title="Home")


@main.route("/about")
def about():
    return render_template("about.html", title="About")
