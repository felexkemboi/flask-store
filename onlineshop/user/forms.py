
from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import PasswordField, StringField, SubmitField, ValidationError, TextAreaField,SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from .. import db

from ..models import Customer,Product,Manufacturer

class ProductForm(FlaskForm):
    name = TextAreaField('Name')
    manufacturer = SelectField('Manufacturer')
    submit = SubmitField(label=('Submit'))

    def __init__(self):
        super(ProductForm, self).__init__()
        self.manufacturer.choices = [(c.id, c.name) for c in Manufacturer.query.all()]
