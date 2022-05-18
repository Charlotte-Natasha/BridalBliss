from flask import render_template,redirect,url_for,abort,request,flash
from app.main import main
from app.models import User,Order,Revieew,Service
from .forms import UpdateProfile,ReviewForm,OrderForm,SelectServiceForm,AddServiceForm
from .. import db
from ..request import get_quotes,setInterval
from flask_login import login_required,current_user
# from ..emails import mail_message
import secrets
import os
from PIL import Image

@main.route('/')
def index():
    quotes = get_quotes()
    # quotes=setInterval(get_quotes,5)
    page = request.args.get('page',1, type = int )
    services = Service.query.order_by(Service.posted.desc()).paginate(page = page, per_page = 3)
    return render_template('index.html', quote = quotes,services=services)
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join('app/static/images', picture_filename)
    form_picture.save(picture_path)
    
    output_size = (200, 200)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_filename

@main.route('/profile',methods = ['POST','GET'])
@login_required
def profile():
    form = UpdateProfile()
    if form.validate_on_submit():
        if form.profile_picture.data:
            picture_file = save_picture(form.profile_picture.data)
            current_user.profile_pic_path = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.bio = form.bio.data
        db.session.commit()
        flash('Succesfully updated your profile')
        return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.bio.data = current_user.bio
    profile_pic_path = url_for('static',filename = 'images/'+ current_user.profile_pic_path) 
    return render_template('profile/profile.html', profile_pic_path=profile_pic_path, form = form)

@main.route('/user/<name>/updateprofile', methods = ['POST','GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save()
        return redirect(url_for('.profile',name = name))
    return render_template('profile/updateprofile.html',form =form)



@main.route('/service/<int:user_id>')
@login_required
def service(user_id):
    user=User.query.get(user_id)
    if user.provider:
        form=AddServiceForm()
        if form.validate_on_submit():
            service=Service()
            service.save()
    render_template('service.html',form=form title='Add service')



