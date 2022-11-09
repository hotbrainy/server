from flask_wtf import FlaskForm
from wtforms import StringField,  BooleanField
from wtforms.validators import DataRequired, Length, Optional
from wtforms.widgets import PasswordInput


class LoginForm(FlaskForm):
    email = StringField('email',  validators=[DataRequired(), Length(min=1, max=100)])
    password = StringField('password',  widget=PasswordInput(hide_value=False),  validators=[DataRequired(), Length(min=6,max=100)])
    remember_me = BooleanField('remember_me', default=False)
    # recaptcha = RecaptchaField()


class SignUpForm(FlaskForm):
    pass
    # recaptcha = RecaptchaField()





