__author__ = 'joe'
# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    app.run()
@app.route('/index')
def index():
    user = {'nickname': "Joe"}
    return render_template("index.html",
                           title="Home",
                           user=user)