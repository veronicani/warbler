from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Email, Length, URL, Optional


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField('text', validators=[InputRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField(
        'Username',
        validators=[InputRequired(), Length(max=30)],
    )

    email = StringField(
        'E-mail',
        validators=[InputRequired(), Email(), Length(max=50)],
    )

    password = PasswordField(
        'Password',
        validators=[InputRequired(), Length(min=6, max=50)],
    )

    image_url = StringField(
        '(Optional) Image URL',
        validators=[Optional(), URL(), Length(max=255)]
    )


class UserEditForm(FlaskForm):
    """Form for editing a user."""

    username = StringField(
        'Username',
        validators=[Optional(), Length(max=30)],
    )

    email = StringField(
        '(Optional) E-mail',
        validators=[Optional(), Email(), Length(max=50)],
    )

    image_url = StringField(
        '(Optional) Image URL',
        validators=[Optional(), URL(), Length(max=255)]
    )

    header_image_url = StringField(
        '(Optional) Header Image URL',
        validators=[Optional(), URL(), Length(max=255)]
    )

    bio = TextAreaField(
        '(Optional) Bio',
        validators=[Optional()],
    )
    
    # Not sure if want ability to edit location - not noted in specs
    # location = StringField(
    #     '(Optional) Location',
    #     validators=[Optional(), Length(max=30)],
    # )

    password = PasswordField(
        'Password',
        validators=[InputRequired(), Length(min=6, max=50)],
    )






class LoginForm(FlaskForm):
    """Login form."""

    username = StringField(
        'Username',
        validators=[InputRequired(), Length(max=30)],
    )

    password = PasswordField(
        'Password',
        validators=[InputRequired(), Length(min=6, max=50)],
    )


class CSRFProtectForm(FlaskForm):
    """Form just for CSRF Protection."""
