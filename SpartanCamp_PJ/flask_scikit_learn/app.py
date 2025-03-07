from flask import Flask
from flask import render_template
from flask import request
import pickle
import numpy as np


# Flaskオブジェクトの生成
app = Flask(__name__)


@app.route("/")
def index():
    """ GET
    return: index.html
    """
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    """ POST
    return: result.html, result
    """
    # 画面入力値を取得する
    predict = int(request.form["predict"])
    # 学習済みのファイルを読み込む
    with open("predict_population.pickle", mode="rb") as fp:
        model = pickle.load(fp)
    # 予測
    result = model.predict(np.array([[predict]]))
    # print(type(result))
    return render_template("result.html", result=round(result[0]))


if __name__ == "__main__":
    app.run(debug=True)
