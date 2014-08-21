from systemofrecord import db
from sqlalchemy.dialects.postgresql import  JSON
import json

class Title(db.Model):

    __tablename__ = 'titles'

    id = db.Column(db.Integer, primary_key=True)
    title_number = db.Column(db.String(64))
    data = db.Column('data', JSON)

    def __init__(self, title_number, data):
        self.title_number = title_number
        self.data = data

    def __repr__(self):
        return "Title id: %d title number: %s data: %s" % (self.id, self.title_number, self.data)

    def as_dict(self):
        #return {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return {'title': {
            'title_number': self.title_number,
            'data': json.loads(self.data)
            }}
