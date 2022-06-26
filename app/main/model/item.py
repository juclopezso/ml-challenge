from .. import db

class Item(db.Model):
    """ Item Model for storing item related details """
    __tablename__ = "item"

    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=True, default=None)
    start_time = db.Column(db.DateTime, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=True, default=None)
    nickname = db.Column(db.String(255), unique=True, index=True)

    def __repr__(self):
        return "<Item {}-{}>".format(self.site, self.id)