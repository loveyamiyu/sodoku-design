#from msilib.schema import CheckBox
from asyncio.proactor_events import _ProactorBaseWritePipeTransport
from flask_wtf import FlaskForm
from sqlalchemy import false
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length,ValidationError
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

    def validate(self):
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            raise ValidationError('Invalid username')
        if not user.check_password(self.password.data):
            raise ValidationError('Invalid password')
        return True

        """

    def validate_username(self, username):

        user = User.query.filter_by(username = self.username.data).first() 

        if not user:

            raise ValidationError('Invalid username')
    
    def validate_password(self, password):

        password = User.query.filter_by(password = self.password.data).first() 

        if not password:

            raise ValidationError('Invalid password') """

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40)])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')
    
    def validate(self):
        initial_validation = super(RegistrationForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append("Username taken, please pick a different one")
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already in use, please try a different one or reset password")
            return False
        return True   
    """
    def validate_username(self, username):

        user = User.query.filter_by(username = self.username.data).first() 

        if user is not None:

            raise ValidationError("Username taken, please pick a different one")

    def validate_email(self, email):

        email = User.query.filter_by(email = self.email.data).first() 

        if email is not None:

            raise ValidationError("Email already in use, please try a different one or reset password")
        """