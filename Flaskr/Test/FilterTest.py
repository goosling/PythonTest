__author__ = 'joe'
# -*- coding: utf-8 -*-

from flask import Flask
import unittest

app = Flask(__name__)

@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]

def reverse_filter(s):
    return s[::-1]

app.jinja_env.filters['reverse'] = reverse_filter

# 环境处理器,在模版中，g总是存在的
@app.context_processor
def inject_user():
    return dict(user=g.user)

# 传递值不仅仅局限于变量，还可以传递函数
@app.context_processor
def utility_processor():
    def format_price(amount, currency='$'):
        return u'{0:.2f}{1}'.format(amount, currency)
    return dict(format_price=format_price)
