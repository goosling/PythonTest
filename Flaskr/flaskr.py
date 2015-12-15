__author__ = 'joe'
# -*- coding: utf-8 -*-

import sqlite3
from flask import Flask, request, session, g, \
    redirect, render_template, flash, url_for, abort


# 添加数据库初始化函数
from contextlib import closing


# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# 创建应用,设置Flask—WTF，from_object() 会
# 查看给定的对象（如果该对象是一个字符串就会 直接导入它），
# 搜索对象中所有变量名均为大字字母的变量。
app = Flask(__name__)
app.config.from_object(__name__)

# 通常从一个配置文件中导入配置是比较好的做法，
# app.config.from_envvar("Flaskr_SETTINGS", silent=True)


# 建立一个用来初始化数据库的函数
def init_db():
    # closing函数帮助在代码块中数据库连接一直打开
    with closing() as db:
        with app.open_resource('schemal.sql', mode='r') as f:
            db.cursor().executescripts(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    g.db.close()

# 显示条目
@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id DESC ')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

# 添加一个新条目
@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries(title, text) values (?, ?)',
                 [request.form['title'], request.title['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

# 登录和注销
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash("You were logged in")
            return redirect(url_for("show_entries"))
    return render_template('login.html', error=error)

@app.route('/logout')
# 如果你使用 字典的 pop() 方法并且传递了第二个参数（键的缺省值），
# 那么当字典中有 这个键时就会删除这个键，否则什么也不做
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == "__main__":
    app.run()
