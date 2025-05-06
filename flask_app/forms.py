from ast import Pass
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, HiddenField
from wtforms.validators import (
    InputRequired,
    Length,
    Email,
    EqualTo,
    ValidationError,
)


from .models import User


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1, max=40)]
    )
    email = StringField(
        "Email",
        validators=[InputRequired(), Email()]
    )
    password = StringField(
        "Password",
        validators=[InputRequired(), Length(min=6)]
    )
    confirm_password = StringField(
        "Confirm Password",
        validators=[InputRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

    def validate_username(self, field):
        if User.objects(username=field.data).first():
            raise ValidationError("That username is already taken.")

    def validate_email(self, field):
        if User.objects(email=field.data).first():
            raise ValidationError("That email is already registered.")


class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1, max=40)]
    )
    password = StringField(
        "Password",
        validators=[InputRequired()]
    )
    submit = SubmitField("Log In")


class StockSearchForm(FlaskForm):
    ticker = StringField(
        "Ticker Symbol",
        validators=[InputRequired(), Length(min=1, max=10)]
    )
    submit = SubmitField("Search")


class AddToWatchlistForm(FlaskForm):
    ticker = HiddenField(validators=[InputRequired(), Length(min=1, max=10)])
    submit = SubmitField("Add to Watchlist")


class RemoveFromWatchlistForm(FlaskForm):
    ticker = HiddenField(validators=[InputRequired(), Length(min=1, max=10)])
    submit = SubmitField("Remove")

class UpdateProfilePicForm(FlaskForm):
    picture = FileField("Profile Picture", validators=[FileRequired(), FileAllowed(["jpg", "png"], "File does not have an approved extension: jpg, png")])
    submit_picture = SubmitField("Update")