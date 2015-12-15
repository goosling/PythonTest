__author__ = 'joe'
# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    pass

@app.route('/login')
def login():
    pass

@app.route('/user/<username>')
def profile(username):
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()


# 模版渲染例子
@app.route('/hello/')
@app.route('hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# safe过滤
from flask import Markup
Markup('<strong>Hello %s</strong>') % '<blink>hacker</hacker>'
Markup.escape('<blink>hacker</blink>')
Markup.escape('<em>Marked up</em> &raquo; html').striptags()

# 请求对象
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # 如果请求是GET或验证未通过就实现下面代码
    return render_template('login.html', error=error)

# 文件上传
# 想要获取文件上传前其在客户端中的值，可以使用filename()属性，但是其可以伪造
# 最好使用secure_filename()函数
from werkzeug import secure_filename
@app.route('upload', method=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('var/www/uploads/upload_file.txt')
    #   f.save('var/www/uploads/'+ secure_filename(f.filename))

# cookies
@app.route('/')
# 读取cookies
def index():
    username = request.cookies.get('username')
    # 使用 cookies.get(key)代替cookies[key]
    # 以避免当cookie不存在引发keyerror

# 存储cookie
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp

# 重定向和错误
from flask import abort, redirect, url_for
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_excuted()

@app.error_handler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

# session会话,使用之前必须先设置一个密钥
from flask import Flask, session, redirect, url_for, escape, request

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', method=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
        <p><input type=text name=username>
        <p><input type=submit value=Login>
        </form>
    '''
# 如果会话中有用户名就删除它
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

# 设置密钥，复杂一点
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# 继承WSGI中间件
from werkzeug.contrib.fixers import LighttpdCGIRootFix
app.wsgi_app = LighttpdCGIRootFix(app.wsgi_app)


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
