from flask_wtf import FlaskForm
from wtforms import PasswordField,TextField

class LoginForm(FlaskForm):
    username=TextField('username')
    password=PasswordField('password')
