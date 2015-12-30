__author__ = 'joe'
# -*- coding: utf-8 -*-

from flask import Flask
# 每个web表单都继承自Form的类
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
