from flask_wtf import FlaskForm
from wtforms import  SubmitField , TextAreaField,SelectField 
from ..models import Manufacturer 

class ProductForm(FlaskForm):
    name = TextAreaField('Name')
    manufacturer = SelectField('Manufacturer')
    submit = SubmitField(label=('Submit'))

    def __init__(self):
        super(ProductForm, self).__init__()
        self.manufacturer.choices = [(c.id, c.name) for c in Manufacturer.query.all()]