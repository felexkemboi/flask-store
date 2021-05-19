
from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import PasswordField, StringField, SubmitField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Customer,Product


class ProductForm(FlaskForm):
    name = TextAreaField('Name', validators=[DataRequired()])
