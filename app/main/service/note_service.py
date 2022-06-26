import datetime
from app.main import db
from app.main.model.note import Note


def save_new_note(data):
    note = Note.query.filter_by(title=data['title']).first()
    if not note:
        new_note = Note(
            title=data['title'],
            description=data['description'],
            created_at=datetime.datetime.utcnow()
        )
        save_changes(new_note)
        response_object = {
            'status': 'success',
            'message': 'Note successfully created.'
        }
        return response_object, 201 # created
    else:
        response_object = {
            'status': 'fail',
            'message': 'Note already exists',
        }
        return response_object, 409 # conflict


def get_notes():
    return Note.query.all()


def get_note(id):
    return Note.query.filter_by(id=id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()