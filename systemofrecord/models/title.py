from sqlalchemy import Integer, Column, String, Sequence
from sqlalchemy.dialects.postgresql import JSON
import json

from systemofrecord import db


class Title(db.Model):
    __tablename__ = 'title'

    id = Column(Integer, Sequence('title_id_seq'), primary_key=True)
    title_number = Column(String(64))
    creation_timestamp = Column(Integer)
    data = Column('data', JSON)
    blockchain_index = Column(Integer, Sequence('blockchain_index_seq'))

    def __init__(self, title_number, creation_timestamp, data, blockchain_index=None):
        self.title_number = title_number
        self.data = data
        self.creation_timestamp = creation_timestamp
        self.blockchain_index = blockchain_index

    def __repr__(self):
        return "Title id: %d title number: %s data: %s blockchain_index: %s creation_timestamp: %d" % (
            self.id,
            self.title_number,
            self.data,
            self.blockchain_index,
            self.creation_timestamp
        )

    def as_dict(self):
        return {
            'title': {
                'title_number': self.title_number,
                'creation_timestamp': self.creation_timestamp,
                'blockchain_index': self.blockchain_index,
                'data': json.loads(self.data)
            }
        }