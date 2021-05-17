
#http://docs.sqlalchemy.org/en/latest/core/type_basics.html#generic-types

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from notesApp import db #, login_manager


class Note(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturers.id'), nullable=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Product: {0}\n{1}>'.format(self.name)

class Contract(db.Model):

    __tablename__ = 'contracts'

    id = db.Column(db.Integer, primary_key=True)
    card_info = db.Column(db.Integer)
    bill_number = db.Column(db.Integer, db.ForeignKey('bills.id'), nullable=True)


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Product: {0}\n{1}>'.format(self.name)


class Customer(UserMixin, db.Model):
    """
    Create an Employee table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True, unique=True)
    type = db.Column(db.String(60))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


    def __repr__(self):
        return '<Customer name is: {}>'.format(self.name)


class Delivery(db.Model):

    __tablename__ = 'deliveries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True, unique=True)
    tracking_number = db.Column(db.Integer, primary_key=True)


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Delivery company: {0}\n{1}>'.format(self.name)





class Role(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    users = db.relationship('Customer', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)
