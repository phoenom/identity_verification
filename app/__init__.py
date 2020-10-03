import os

from flask import Flask, render_template

# def create_app(test_config=None):
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# @app.route('/hello')
# def hello():
#     return "Hello World"

@app.route('/')
def index():
    return render_template("index.html", image="static/pentol.png")


@app.route('/new-label')
def label():
    print("oke")
    # print(os.getcwd())
    # return render_template("index.html", image="static/pentol.png")

