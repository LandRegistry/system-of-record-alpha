from sqlalchemy import Integer, Column, String, Sequence
from sqlalchemy.dialects.postgresql import BYTEA
import simplejson

from systemofrecord.services.compression_service import decompress
from systemofrecord import db


class BlockchainObject(db.Model):
    __tablename__ = 'blockchain'

    id = Column(Integer, Sequence('object_id_seq'), primary_key=True)
    object_id = Column(String)
    creation_timestamp = Column(Integer)
    data = Column('data', BYTEA)
    blockchain_index = Column(Integer, Sequence('blockchain_index_seq'))

    def __init__(self, object_id, creation_timestamp, data, blockchain_index=None):
        self.object_id = object_id
        self.data = data
        self.creation_timestamp = creation_timestamp
        self.blockchain_index = blockchain_index

    def __repr__(self):
        return "object id: %d title number: %s data: %s blockchain_index: %s creation_timestamp: %d" % (
            self.id,
            self.object_id,
            self.data,
            self.blockchain_index,
            self.creation_timestamp
        )

    def as_dict(self):
        obj = simplejson.loads(decompress(self.data))
        info = obj['object_info']
        assert info

        info['db_id'] = self.id
        info['creation_timestamp'] = self.creation_timestamp
        info['blockchain_index'] = self.blockchain_index

        return obj