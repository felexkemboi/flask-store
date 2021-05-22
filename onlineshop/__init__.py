
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    Bootstrap(app)
    db = MySQL(app)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint)

    return app
