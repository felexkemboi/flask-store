from flask import abort, render_template, request, jsonify
#from flask_login import current_user, login_required
from . import home
from onlineshop.models import *

@home.route('/')
def homepage():
    return render_template('home/index.html', title="Welcome")

@home.route('/dashboard')
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")

@home.route('/admin/dashboard')
def admin_dashboard():
    return render_template('home/admin_dashboard.html', title="Dashboard")

@home.route('/tables')
def viewtables():
    return render_template("home/view_tables.html")

@home.route('/gettables', methods=['GET'])
def gettables():

    table =  str(request.args.get('mytable')).lower()

    if table == 'user':
        ideas = User.query.order_by('username')
        return getTable(ideas)
    if table == 'career':
        ideas = Career.query.all()
        return getTable(ideas)
    if table == 'role':
        ideas = Role.query.all()
        return getTable(ideas)
    if table == 'note':
        ideas = Note.query.all()
        return getTable(ideas)
    else:
        error = {
            'status': '404',
            'msg': 'unable to retrieve ideas'
        }
        return jsonify(error)

def getColumns(modelclass):
    from sqlalchemy import inspect
    mapper = inspect(modelclass)
    return [c.key for c in mapper.attrs]

def getTable(ideas):
    # ideas = User.query.order_by('username')
    # d = [i.serialize() for i in ideas]

    if ideas:
        m = []
        querylist = []
        for i in ideas:
            try:
                q = i.serialize()
                querylist.append(q)
            except:
                m.append('error')

        data = {
            'status': 'OK',
            'ideas': querylist,
            'msg': m
        }
        return jsonify(data)
    else:
        error = {
            'status': 404,
            'ideas': None,
            'msg': 'unable to retrieve ideas'
        }
        return jsonify(error)
