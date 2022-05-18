from . import main_blueprint
from flask import render_template
from .forms import LogIn, Signup

@main_blueprint.route('/')
def index():
    return render_template('about.html')

@main_blueprint.route('/login')
def login():
    form=LogIn()
    return render_template('login.html', form=form)    