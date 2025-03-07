from flask import Flask
from flask import render_template


# Flaskのtemplatesやstaticの置き場を変えたい時は
# Flaskオブジェクトを生成するときに指定することでデフォルト設定を変更できる
app = Flask(__name__, static_folder="parts/static", template_folder="parts/templates")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
