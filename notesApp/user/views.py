from flask import redirect, render_template, url_for
from . import user
from .forms import ProductForm
from .. import db

@user.route('/products')
def products():
    products = db.engine.execute("SELECT pr.name 'name', mn.name 'manufacturer' FROM products pr LEFT JOIN manufacturers mn ON pr.manufacturer_id = mn.id")
    return render_template('user/products.html', products=products)

@user.route('/products/add', methods=['GET', 'POST'])
def add_products():
    form = ProductForm()
    if form.validate_on_submit():
        try: 
            db.engine.execute("INSERT INTO products(name,manufacturer_id) VALUES(%s, %s)",(str(form.name.data), int(form.manufacturer.data)))
        except Exception as error:
            pass
        return redirect(url_for('user.add_products'))
    return render_template('user/note.html', form=form, title='Add Product')


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
#         return redirect(url_for('products'))
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
#     return redirect(url_for('products'))
#
#     return render_template(title="Delete Note")
