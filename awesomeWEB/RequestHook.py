__author__ = 'joe'
# -*- coding: utf-8 -*-

from flask import Flask
from flask import make_response
from flask import redirect
from flask import abort


app = Flask(__name__)


# 状态码400，请求无效
@app.route('/')
def index():
    response = make_response("<h1>This document carries a cookie!</h1>")
    response.set_cookie('answer', 42)
    return response

# 重定向,状态码302
@app.route('/')
def index():
    return redirect('www.example.com')

# 状态码404，返回未知页面
@app.route('/user/<username>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name

