import os
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_login import LoginManager
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user

from database import User


# Flaskオブジェクトの生成
app = Flask(__name__)

# ログイン機能実装の必須アイテム
app.config["SECRET_KEY"] = os.urandom(24)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return User.get(id=int(id))


@login_manager.unauthorized_handler
def unauthorized():
    return redirect("/login")


@app.route("/")
@login_required
def index():
    """ GET
    return: index.html
    """
    return render_template("index.html")


@app.route("/login")
def login():
    """ GET
    return: login.html
    """
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    """ POST
    return: 
    """
    name = request.form["userName"]
    password = request.form["password"]
    user = User.get(name=name)

    if check_password_hash(user.password, password):
        login_user(user)
        return redirect("/")
    return redirect("/login")


@app.route("/signup")
def signup():
    """ GET
    return: signup.html
    """
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def register():
    """ POST
    return: redirect to login.html
    """
    # 画面の入力値を取得する
    name = request.form["userName"]
    password = request.form["password"]

    # パスワードの暗号化し、DBに登録する
    User.create(
        name=name, 
        password=generate_password_hash(password, method="sha256")
        )
    return redirect("/login")


@app.route("/logout", methods=["POST"])
def logout():
    """ POST
    return: redirect to login.html
    """
    logout_user()
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
