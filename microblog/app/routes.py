#!/usr/bin/env python3
"""Home page route """
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
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
