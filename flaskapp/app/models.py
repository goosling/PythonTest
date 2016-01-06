__author__ = 'joe'
# -*- coding: utf-8 -*-

# 密码散列
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin


class User(UserMixin, db.Model):
    password_hash = db.column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    # 修改user模型，支持用户登录
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
