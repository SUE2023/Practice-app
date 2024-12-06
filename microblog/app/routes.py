#!/usr/bin/env python3
"""Home page route """
from flask import render_template,  flash, redirect
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user,logout_userlogout_user
import sqlalchemy as sa
from app import db
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Mercy'}
    posts = [
        {
            'author': {'username': 'Veronica'},
            'body': 'Experience of 2024 Retreats!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Experience of Leadership!'
        },
         {
            'author': {'username': 'John Paul'},
            'body': 'All things are gifts!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
