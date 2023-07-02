from flask_wtf import FlaskForm, RecaptchaField
# from wtforms import Form نکته های بیشتری دارد برای پیاده سازی
from wtforms import StringField, EmailField, PasswordField, BooleanField, DateField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from blog.models import User, Post
import datetime


class RegisterForm(FlaskForm):
    """ form for user register """
    username = StringField(label='username', validators=[DataRequired()])
    email = EmailField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='password', validators=[DataRequired()])
    confirm_pass = PasswordField(label='confirm pass',
                                  validators=[EqualTo('password', message='password must be equal confirm password'), DataRequired()])
    field_recap = RecaptchaField(label='test')
    
    def validate_username(self, username):
        """ validation for username """
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username exist')


class LoginForm(FlaskForm):
    """ form for create login form """
    username = StringField(label='username', validators=[DataRequired()])
    password = PasswordField(label='password', validators=[DataRequired()])
    remember = BooleanField(label='remember me')

class CreatePostForm(FlaskForm):
    """ form for create post"""
    title = StringField(label="title", validators=[DataRequired()])
    date = DateField(label="Date", default=datetime.datetime.now)
    content = TextAreaField(label="content",validators=[DataRequired()])

    def validate_title(self, title):
        """ don't be duplicate title """
        per_title = Post.query.filter_by(title=title.data).first()
        if per_title:
            raise ValidationError('This title exist')
