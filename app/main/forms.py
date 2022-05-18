from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,EqualTo,Email
from wtforms.widgets import TextArea
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,TextAreaField, SubmitField,ValidationError,DateTimeField,SelectField,IntegerField
from wtforms.validators import DataRequired,Email,Length
from flask_login import current_user
from ..model import User

class Signup(FlaskForm):
    username = StringField(label='Enter username', validators=[DataRequired(),Length(min=3,max=200)])
    email = EmailField(label='Enter your email', validators=[DataRequired(),Email()])
    password = PasswordField(label='Enter password', validators=[DataRequired(),Length(min=5,max=150)])
    confirm_password = PasswordField(label='Confirm password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField(label='Sign up')

class LogIn(FlaskForm):
    username = StringField(label='Enter username', validators=[DataRequired(),Length(min=3,max=200)])
    password = PasswordField(label='Enter password', validators=[DataRequired(),Length(min=5,max=150)])  
    remember = BooleanField('Remember me')
    submit = SubmitField(label='Log In')

class UpdateProfile(FlaskForm):
    username = StringField('Enter Your Username', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(),Email()])
    bio = TextAreaField('Write a brief bio about you.',validators = [DataRequired()])
    profile_picture = FileField('profile picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            if User.query.filter_by(email = email.data).first():
                raise ValidationError("The Email has already been taken!")
    
    def validate_username(self, username):
        if username.data != current_user.username:
            if User.query.filter_by(username = username.data).first():
                raise ValidationError("The username has already been taken")

class OrderForm(FlaskForm):
    Details = TextAreaField('Blog Content',validators=[DataRequired()])
    devilerydate= DateTimeField('Delivery date',validators=[DataRequired()])
    submit = SubmitField('Order Now')


class ReviewForm(FlaskForm):
    review=TextAreaField('Leave a Review', validators=[DataRequired()])
    submit = SubmitField('Submit Details')


class SelectServiceForm(FlaskForm):
    category=SelectField('choose service category', choices=[('Photography', 'photography'), ('Catering', 'catering'), ('Transport', 'transport')])
    budget=IntegerField('Enter amount not less than Ksh 50,000', validators=[DataRequired(),Length(min=50000)])
    delivery_date=DateTimeField('Expected date of delivery', validators=[DataRequired()])
    submit=SubmitField('Submit Details')


class AddServiceForm(FlaskForm):
    category=SelectField('choose service category', choices=[('Photograpy', 'photograpy'), ('Catering', 'catering'), ('Transport', 'transport')])
    cost=IntegerField('Enter service cost in kenyan shillings', validators=[DataRequired()])
    service_pic=FileField('profile picture', validators=[FileAllowed(['jpg','png'])])
    description=TextAreaField("Give a brief description of the service")
    submit=SubmitField('Submit')
