from flask_restx import Api
from flask import Blueprint

from .main.controller.note_controller import api as note_ns
from .main.controller.item_controller import api as item_ns 

blueprint = Blueprint('api', __name__)

api = Api(
  blueprint,
  title='FLASK REST API FOR ML',
  version='1.0',
  description='FLASK REST API for consuming ML APIs items and notes',
)

# namespaces
api.add_namespace(note_ns, path='/notes')
api.add_namespace(item_ns, path='/items')