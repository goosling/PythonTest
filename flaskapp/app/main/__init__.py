__author__ = 'joe'
# -*- coding: utf-8 -*-
from flask import Blueprint, Flask
main = Blueprint('main', __name__)

from . import views, errors
