__author__ = 'joe'
# -*- coding: utf-8 -*-

from flask import Flask, render_template, session, redirect, url_for, flash
app = Flask(__name__)

# 定义表单类
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

@app.route('/flash', methods=['GET', 'POST'])
def index1():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name')
        session['name'] = form.name.data
        return redirect(url_for('index1'))
    return render_template('index.html', form=form, name=session.get('name'))


from flask.ext.sqlalchemy import SQLAlchemy
import os

# 配置数据库
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

# 定义模型，定义role和user模型
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 关系
    users = db.relationship('Users', backref='role')

    def __repr__(self):
        return '<Role %r>' %self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    # 关系,使用users表中的外键链接了两行
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' %self.username


db.create_all()
db.drop_all()

# 创建角色和用户
admin_role = Role(name="Admin")
mod_role = Role(name='Moderator')
user_role = Role(name='User')
user_john = User(username="John", role=admin_role)
user_susan = User(username='Susan', role=mod_role)
user_joe = User(username='Joe', role=user_role)
# 添加到会话中
db.session.add(admin_role)
db.session.add(mod_role)
db.session.add(user_role)
db.session.add(user_john)
db.session.add(user_joe)
db.session.add(user_susan)
# db.session.add_all([admin_role, mod_role, user_role, user_john, user_susan, user_joe])
# 加入之后需要提交会话
db.session.commit()

print(admin_role.id)# 1
print(admin_role.id)# 2
print(admin_role.id)# 3

# 删除行 db.session.delete(...)


# 配置migrate
from flask.ext.migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)
....add_command('db', MigrateCommand)


# 配置flask-mail发送gmail
# 不要把账户密码等直接写入脚本。需要从脚本环境中导入敏感信息
app.config['MAIL_SERVER'] = 'smtp.goolemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

# 初始化flask-mail
from flask.ext.mail import Mail
mail = Mail(app)

# 电子邮件支持
from flask.ext.mail import Message

app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[FLASKY]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'

def send_mail(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX']+subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template+'.txt', **kwargs)
    msg.html = render_template(template+'.html', **kwargs)
    mail.send(msg)



# 异步发送邮件
from threading import Thread

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_mail(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX']+subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template+'.txt', **kwargs)
    msg.html = render_template(template+'.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr