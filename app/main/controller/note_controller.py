from flask import request
from flask_restx import Resource
from ..util.dto import NoteDto
from ..service.note_service import get_notes, get_note, save_new_note

api = NoteDto.api
_note = NoteDto.note

# decorator for route resources
@api.route('/')
class NoteList(Resource):
    # decorator to add API documentation
    @api.doc('list_of_notes')
    # decorator to specify the fields to use for serialization
    # could be used @api.marsahl_with(_note, as_list=True)
    @api.marshal_list_with(_note, envelope='data')
    def get(self):
        return get_notes()

    # decorator to specify on of the expected responses
    @api.response(201, 'Note successfully created.')
    @api.doc('create a new note')
    # decorator to specify the expected input model
    @api.expect(_note, validate=True)
    def post(self):
        data = request.json
        return save_new_note(data=data)


# route with id param
@api.route('/<id>')
# decorator to specify the expected parameters
@api.param('id', 'The note identifier')
@api.response(404, 'Note not found.')
class User(Resource):
    @api.doc('get a note')
    @api.marshal_with(_note)
    def get(self, id):
        note = get_note(id)
        if not note:
            api.abort(404)
        else:
            return note