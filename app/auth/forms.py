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