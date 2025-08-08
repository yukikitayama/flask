from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hi</h1>"


@app.route("/information")
def info():
    return "<h1>Info</h1>"


@app.route("/user/<name>")
def user(name):
    return f"<h1>100th letter: {name[100]}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
