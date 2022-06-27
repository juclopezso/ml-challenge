from .. import db

class Item(db.Model):
    """ Item Model for storing item related details """
    __tablename__ = "item"

    pk = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.Integer)
    site = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=True, default=None)
    start_time = db.Column(db.DateTime, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=True, default=None)
    nickname = db.Column(db.String(255), index=True)

    def __repr__(self):
        return "<Item {}-{}. Seller {}>".format(self.site, self.id, self.nickname)