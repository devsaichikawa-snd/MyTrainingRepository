from flask import Flask
from flask import render_template
from flask import request
from PIL import Image
import pyocr


# Flaskオブジェクトの生成
app = Flask(__name__)
# オブジェクトの生成
tools = pyocr.get_available_tools()
# tesseractを格納
tool = tools[0]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ocrFlask", methods=["POST"])
def ocr_flask():
    file = request.files["uploadFile"]
    img = Image.open(file)
    img.save("static/images/ocr_flask.png")
    text = tool.image_to_string(
        img, lang="eng+jpn", builder=pyocr.builders.TextBuilder()
    )
    return render_template("ocrFlask.html", text=text)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)


"""先生の模範解答
from flask import Flask
from flask import render_template
from flask import request
from PIL import Image
import pyocr


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=[POST])
def upload():
    ocr_file = request.get["ocrFile"] # form値(file)を取得する→アップロードファイル
    img = Image.open(ocr_file)
    tools = pyocr.get_available_tools()
    tool = tools[0]
    text = tool.image_to_string(
        img,
        lang="eng+jpn",
        builder=pyocr.builders.TextBuilder()
    )
    return render_template("index.html", text=text)

if __name__ == "__main__":
    app.run()

"""
