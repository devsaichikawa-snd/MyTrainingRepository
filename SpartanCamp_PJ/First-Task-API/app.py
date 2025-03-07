""" 要件
1. 猫、犬、狐の画像が表示される以下のAPIを利用して、以下のgifのように選択した動物の画像が表示されるようにしてください。
"""
import json
import requests
import secrets
from flask import Flask
from flask import render_template
from flask import request


# Flaskオブジェクトの生成
app = Flask(__name__)


# セッション情報を暗号化するためのキー設定
app.secret_key = secrets.token_urlsafe(32)


@app.route("/")
def index():
    """GET index"""
    return render_template("index.html")


# 利用APIをdictに格納
api_url = {
    "cat": "https://api.thecatapi.com/v1/images/search",
    "dog": "https://dog.ceo/api/breeds/image/random",
    "fox": "https://randomfox.ca/floof",
}

# HTML select要素のname属性を指定
select_result = "selectAnimal"


@app.route("/animal", methods=["POST"])
def animal():
    """POST animal
    index.htmlで選択されたselect要素を受け取り、判定結果でAPIを出しわける
    """
    if request.form[select_result] == "cat":
        # 猫を選んだ
        res = requests.get(api_url["cat"])
        outfile = json.loads(res.text)[0]["url"]
    elif request.form[select_result] == "dog":
        # 犬を選んだ
        res = requests.get(api_url["dog"])
        outfile = json.loads(res.text)["message"]
    elif request.form[select_result] == "fox":
        # 狐を選んだ
        res = requests.get(api_url["fox"])
        outfile = json.loads(res.text)["image"]
    else:
        return ""
    return render_template("animal.html", outfile=outfile)


if __name__ == "__main__":
    app.run(debug=True)
