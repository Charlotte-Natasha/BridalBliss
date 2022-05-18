from flask import render_template
from .forms import LogIn, Signup  
from app import auth



@auth.route('/')
def index():
    return render_template('about.html')

@auth.route('/login')
def login():
    form=LogIn()
    return render_template('login.html', form=form)  