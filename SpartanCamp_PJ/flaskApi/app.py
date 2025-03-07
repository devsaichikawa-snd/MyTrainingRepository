from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route("/")
def hello():
    data = {"name": "satoshi", "age": 28, "message": "Hello API"}
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
