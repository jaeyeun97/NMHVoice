from flask_wtf  import Form
from wtforms import StringField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Email, Length


class SignUpForm(Form):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     EqualTo('confirm','Passwords do not match'),
                                                     Length(min=7,message='Password has to be longer than 7 characters')])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('confirm','Passwords do not match')])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm',message='Passwords do not match')])
    tos = BooleanField('Terms of Service', validators=[DataRequired()])

    def validate_email(form, field):
        if(field.data.split('@')[1] != "nmhschool.org"):
            raise ValidationError("It has to be a NMH provided email address")


class SignInForm(Form):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me', default=False)
    
