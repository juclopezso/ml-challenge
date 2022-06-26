from .. import db

class Note(db.Model):
    """ Note Model for storing note related details """
    __tablename__ = "note"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    starred = db.Column(db.Boolean, nullable=True, default=False)
    description = db.Column(db.String(2000), nullable=True, default=None)
    created_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Note '{}'>".format(self.title)