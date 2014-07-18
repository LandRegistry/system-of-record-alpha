from systemofrecord import db
from sqlalchemy.dialects.postgresql import  TEXT

class Titles(db.Model):

    __tablename__ = 'titles'

    id = db.Column(db.Integer, primary_key=True)
    title_number = db.Column(db.String(64))
    #data = db.Column('data', JSON)
    data = db.Column(TEXT)

    def __init__(self, title_number, data):
        self.title_number = title_number
        self.data = data

    def __repr__(self):
        return "Title id: %d title number: %s data: %s" % (self.id, self.title_number, self.data)
