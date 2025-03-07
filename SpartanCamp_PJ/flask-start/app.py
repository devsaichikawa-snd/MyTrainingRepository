from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Flask"


# @app.route("/satoshi")
# def hiraizumi():
#     return "Hello satoshi"


# @app.route("/user/<name>")
# def heyName(name):
#     return name


# @app.route("/user/age/<age>")
# def heyAge(age):
#     return age


@app.route("/user/<name>/<age>")
def heyNameAge(name, age):
    return name + age


@app.route("/html")
def html():
    # return "<h1>Hello HTML</h1>"
    return render_template("index.html")


@app.route("/html/<name>")
def htmlName(name):
    # return "<h1>Hello HTML</h1>"
    return render_template("name.html", name=name)


@app.route("/html/age/<age>")
def htmlAge(age):
    return render_template("age.html", age=age)


@app.route("/query")
def query():
    search_text = request.args.get("search_text")
    if search_text is not None:
        return search_text
    return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
