from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from  wtforms.validators import (
    DataRequired,
    EqualTo,
    Length,
)
from app import app


class RegisterForm(FlaskForm):
    """User register form"""
    username = StringField(
        'Username',
        validators=[DataRequired()]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6, message="Select a stronger password.")
        ]
    )
    confirm = PasswordField(
        'Confirm Your Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Password must match')
        ]
    )
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    """User login form"""
    username =  StringField(
        'Username',
        validators=[DataRequired(),
        ]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()])
    submit = SubmitField('Login')