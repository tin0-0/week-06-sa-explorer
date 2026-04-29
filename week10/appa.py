# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Pual"

@app.route("/about")
def about():
    return "<h1>About this flask app</h1><p>Built by Tino week 10 of Unicollege.</p>"

if __name__ == "__main__":
    app.run(debug = True)