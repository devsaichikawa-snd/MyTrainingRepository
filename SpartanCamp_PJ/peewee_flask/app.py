from flask import Flask
from flask import render_template
from flask import request

from database import Post


app = Flask(__name__)


@app.route("/")
def index():
    posts = Post.select()
    return render_template("index.html", posts=posts)


@app.route("/create", methods=["POST"])
def create():
    name = request.form["postName"]
    title = request.form["postTitle"]
    body = request.form["postBody"]
    Post.create(name=name, title=title, body=body)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
