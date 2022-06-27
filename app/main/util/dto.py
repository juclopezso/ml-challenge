from email.policy import default
from flask_restx import Namespace, fields, reqparse
from werkzeug.datastructures import FileStorage

from app.main.util.constants import FileConfigEnum


# DTO: data ttransfer object
class NoteDto:
    # flask-restplus provides a Namespace class that is used to create a namespace the API
    api = Namespace('note', description='note related operations')
    note = api.model('note', {
        'title': fields.String(required=True),
        'description': fields.String(description='note description'),
        'starred': fields.Boolean(description='is note starred'),
        'created_at': fields.DateTime(description='note created at'),
    })
    

class ItemDto:
    api = Namespace('item', description='item related operations')
    item = api.model('item', {
        'id': fields.Integer(),
        'site': fields.String(),
        'price': fields.Float(),
        'start_time': fields.DateTime(),
        'name': fields.String(),
        'description': fields.String(),
        'nickname': fields.String()
    })

class ItemCreatetDto:
    parser = reqparse.RequestParser()
    parser.add_argument('file', location='files', type=FileStorage, required=True)
    parser.add_argument('encoding', location='form', help='Encoding of file', default=FileConfigEnum.ENCODING.value)
    parser.add_argument('separator', location='form', help='Separator of file', default=FileConfigEnum.SEPARATOR.value)
