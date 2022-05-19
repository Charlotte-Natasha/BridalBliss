from flask import render_template,redirect,url_for, flash,request
from .forms import LogIn, Signup  
from . import auth
from .. import db
from flask_login import login_user,logout_user,login_required, current_user
from ..model import User

@auth.route('/signup',methods = ["GET","POST"])
def signup():
    form = Signup()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user is None:
            user = User(email = form.email.data, username = form.username.data,password = form.password.data)
            user.save_u()
            
            return redirect(url_for('auth.login'))
        else:
            flash('That username is in use, try a new one')
    return render_template('auth/signup.html', form=form)

@auth.route('/login',methods=['GET','POST'])
def login():
    form=LogIn()
    if form.validate_on_submit():
        user=User.query.filter_by(username = form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))  

        flash('Invalid username or Password')
        
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))