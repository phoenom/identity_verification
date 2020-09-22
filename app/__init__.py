import os

from flask import Flask, render_template

# def create_app(test_config=None):
app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello World"

@app.route('/')
def index():
    print(os.getcwd())
    return render_template("index.html", image="static/pentol.png")

