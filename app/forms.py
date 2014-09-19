from flask.ext.wtf import Form
from app.models import User
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import TextField, BooleanField, SubmitField, PasswordField
from wtforms.validators import Required, EqualTo, DataRequired, Length

class LoginForm(Form):
    username = TextField('Username', validators = [Required(), Length(min=3, max=15)])
    password = PasswordField('Password', validators = [Required(), Length(min=5, max=20)])
    remember_me = BooleanField('remember_me', default = False)

class RegisterForm(Form):
	username = TextField("Team Name", validators = [Required("Username Field Required"), Length(min=3, max=15)])
	password = PasswordField('New Password', validators = [Required("Password Field Required"), Length(min=5, max=20), EqualTo('confirm', message='Passwords must match')])
	confirm = PasswordField('Repeat Password')

class UploadForm(Form):
	upload = FileField("Upload your solution:", validators = [Required("Please choose a file to submit!")])