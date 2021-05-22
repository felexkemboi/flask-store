# app/__init__.py

# third-party imports
from flask import Flask, render_template, abort

#from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import config
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    Bootstrap(app)
    db.init_app(app)

    #migrate = Migrate(app, db)

    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    return app
