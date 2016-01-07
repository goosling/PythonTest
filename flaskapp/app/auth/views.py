__author__ = 'joe'
# -*- coding: utf-8 -*-

from flask import render_template, url_for, request, flash, redirect
from . import auth
from flask.ext.login import login_user
from ..models import User
from .forms import LoginForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)

# 登出用户
from flask.ext.login import logout_user, login_required

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have been logged out')
    return redirect(url_for('main.index'))


# 注册新用户
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

# 确认发送邮件的注册路由
from ..email import send_email
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():

        db.session.add(login_user())
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, 'confirm your account', 'auth/email/confirm',
                   user=user, token=token)
        flash('.....False')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form)

# 确认用户的账户
from flask.ext.login import current_user

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirmed(token):
        flash('you have confirmed your account')
    else:
        flash('the confirmation link is invalid or has expired')
    return redirect(url_for('main.index'))

# 过滤未确认的账户
@auth.before_app_request
def before_request():
    if current_user.is_authenticated() \
        and not current_user.confirmed \
        and request.endpoint[:5] != 'auth.'\
        and request.endpoint != 'static':
    return redirect(url_for('auth.unconfirmed'))

@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_annoymous() or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')

#  重新发送账户确认邮件
@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'confirm your account',
               'auth/email/confirm', user=current_user, token=token)
    flash('A new confirmation email has been send to you by email')
    return redirect(url_for('main.index'))