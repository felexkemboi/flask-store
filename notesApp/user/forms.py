
from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import PasswordField, StringField, SubmitField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Customer


class NoteForm(FlaskForm):
    """
    Adding a note for a user
    """
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Note', validators=[DataRequired()])
    submit = SubmitField('Submit')
