import os
from app.main import create_app, db
from app import blueprint
# models
from app.main.model import note, item

# app stucture: functional structure, consist of organizing the app by pieces by what they do
# blueprint: collection of views, templates, static files and other elements
# that can be appliead to an application
# used to organize the appplication into distintc components. Structrure the app in several smaller apps
app = create_app(os.getenv('FLASK_ENV') or 'dev')
app.register_blueprint(blueprint)
# custom CLI commands
with app.app_context():
    from commands import *

app.app_context().push()

