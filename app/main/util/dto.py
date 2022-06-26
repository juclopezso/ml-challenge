from flask_restx import Namespace, fields


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