__author__ = 'joe'
# -*- coding: utf-8 -*-

from flaskapp import app

@app.route('/')
@app.route('/index')
def index():
    return ""