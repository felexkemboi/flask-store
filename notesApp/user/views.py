from flask import flash, redirect, render_template, url_for, request
from flask_login import login_required, current_user

from . import user
from .forms import ProductForm
from .. import db
from ..models import Product



@user.route('/notes')
def list_notes():
    return render_template('user/notes.html', user='user', notes=notes, title='Notes')

@user.route('/products/add', methods=['GET', 'POST'])
def add_note():
    #user = 'current_user'
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(name=form.name.data)
        try:
            db.session.add(product)
            db.session.commit()
            flash('You have successfully added a product.')
        except:
            flash('Error: .')
        return redirect(url_for('/'))

    return render_template('user/note.html', form=form, title='Add Product') #add_role=add_note,


# @user.route('/viewprofile', methods=['GET', 'POST'])
# def viewprofile():
#     """
#     Handle requests to the /register route
#     Add an notetaker to the database through the registration form
#     """
#     user = current_user
#     form=UserUpdateForm(obj=user)
#     form.populate_obj(user)
#     if form.validate_on_submit():
#
#         form.populate_obj(user)
#
#         db.session.commit()
#
#         flash('You have successfully edited your profile!')
#     return render_template('user/user.html', title="View Profile", user=user, form=form, action='Edit')


# @user.route('/notes/edit/<int:id>', methods=['GET', 'POST'])
# def edit_note(id):
#     add_note = False
#     note = Note.query.get_or_404(id)
#     form = NoteForm(obj=note)
#     if form.validate_on_submit():
#         note.title = form.title.data
#         note.body = form.body.data
#         db.session.add(note)
#         db.session.commit()
#         flash('You have successfully edited the note.')
#
#         # redirect to the roles page
#         return redirect(url_for('user.list_notes'))
#
#     form.body.data = note.body
#     form.title.data = note.title
#     return render_template('user/note.html', add_role=add_note,form=form, title="Edit Note")

# @user.route('/notes/delete/<int:id>', methods=['GET', 'POST'])
# def delete_note(id):
#     """
#     Delete a role from the database
#     """
#
#     note = Note.query.get_or_404(id)
#     db.session.delete(note)
#     db.session.commit()
#     flash('You have successfully deleted the role.')
#
#     # redirect to the roles page
#     return redirect(url_for('user.list_notes'))
#
#     return render_template(title="Delete Note")
