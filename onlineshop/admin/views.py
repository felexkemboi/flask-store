from flask import redirect, render_template, url_for
from . import admin
from .. import db
from .forms import ProductForm

@admin.route('/admin/products')
def admin_products():
    products = db.engine.execute("SELECT pr.name 'name', mn.name 'manufacturer' FROM products pr LEFT JOIN manufacturers mn ON pr.manufacturer_id = mn.id")
    return render_template('admin/products/products.html', products=products)

@admin.route('/products/add', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        try: 
            db.engine.execute("INSERT INTO products(name,manufacturer_id) VALUES(%s, %s)",(str(form.name.data), int(form.manufacturer.data)))
        except Exception as error:
            pass
        return redirect(url_for('admin.add_products'))
    return render_template('user/note.html', form=form, title='Add Product')


@admin.route('/admin/users', methods=['GET', 'POST'])
def list_users():
    users = db.engine.execute("SELECT cs.name 'Name', cs.type 'Type', cont.card_info 'CardInfo', cont.bill_number 'BillNumber', del.name 'DeliveryCo', del.tracking_number 'TrackingNo' FROM customers cs LEFT JOIN contracts cont ON cont.user_id = cs.id LEFT JOIN deliveries del ON del.user_id = cs.id")
    return render_template('admin/users/users.html', users=users, title="Users")


@admin.route('/admin/delete/<int:id>', methods=['GET', 'POST'])
def delete_role(id):
    db.engine.execute("DELETE FROM %s WHERE id = %s"), ("products", id)
    return redirect(url_for('admin.list_roles'))
