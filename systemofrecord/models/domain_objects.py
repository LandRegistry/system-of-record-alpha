from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Sequence, String, ForeignKey

from systemofrecord.repository.message_id_validator import check_object_id_matches_id_in_message

from systemofrecord.services.json_conversion import from_json, to_json

from systemofrecord.services.compression_service import decompress, compress
from systemofrecord import db


class Chain(db.Model):
    __tablename__ = 'chain'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(String)
    record_id = Column(Integer, ForeignKey('blockchain.id'))

    @staticmethod
    def create(chain_name, chain_value):
        return Chain(name=chain_name, value=chain_value)

    def __repr__(self):
        return "tag id: %d name: %s value: %s record_id: %d, record_seq: %d" % (
            self.id,
            self.name,
            self.value,
            self.record_id,
            self.record_seq
        )


class BlockchainObject(db.Model):
    __tablename__ = 'blockchain'

    id = Column(Integer, Sequence('object_id_seq'), primary_key=True)
    object_id = Column(String)
    creation_timestamp = Column(Integer)
    data = Column('data', BYTEA)
    blockchain_index = Column(Integer, Sequence('blockchain_index_seq'))
    chains = relationship('Chain')

    @staticmethod
    def create(object_id, message):
        check_object_id_matches_id_in_message(message, object_id)

        def link_chains():
            try:
                return map(lambda x: Chain.create(x['chain_name'], x['chain_value']), message['object']['chains'])
            except KeyError:
                return []

        return BlockchainObject(
            object_id=object_id,
            creation_timestamp=1,
            data=compress(to_json(message)),
            chains=link_chains()
        )

    def __repr__(self):
        return "object id: %d title number: %s data: %s blockchain_index: %s creation_timestamp: %d chains: %s" % (
            self.id,
            self.object_id,
            self.data,
            self.blockchain_index,
            self.creation_timestamp,
            repr(self.chains)
        )

    def as_dict(self):
        obj = from_json(decompress(self.data))
        info = obj['object']
        assert info

        info['db_id'] = self.id
        info['creation_timestamp'] = self.creation_timestamp
        info['blockchain_index'] = self.blockchain_index

        return obj

