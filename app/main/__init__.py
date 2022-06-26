from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .config import config_by_name

db = SQLAlchemy()
migrate = Migrate()

# using app factory pattern: useful for creating multiple instances of the app with different settings.
# facilitates the creation and swith between different environemnts
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name]())
    db.init_app(app)
    migrate.init_app(app, db)

    return app