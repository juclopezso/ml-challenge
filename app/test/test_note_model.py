import unittest
import datetime
from app.main import db
from app.main.model.note import Note
from app.test.base import BaseTestCase


class TestNoteModel(BaseTestCase):

    def test_note_create(self):
        note = Note(
            title='Note test',
            description='Note test test',
            created_at=datetime.datetime.utcnow()
        )
        db.session.add(note)
        db.session.commit()
        # rerieve saved note
        note_db = Note.query.filter_by(title='Note test').first()
        self.assertTrue(note == note_db and note.id == note_db.id)


if __name__ == '__main__':
    unittest.main()