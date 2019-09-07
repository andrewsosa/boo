import os
from flask import Flask
from flask_migrate import Migrate
from .db import db
from .api import api_blueprint


def create_app(config: str = "boo.config.Default") -> Flask:
    """ Create an instance of the Flask application """
    app = Flask(__name__)
    app.config.from_object(config)

    # Setup db
    db.init_app(app)
    db.create_all(app=app)
    migrate = Migrate(app, db)

    # Register blueprints
    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app
