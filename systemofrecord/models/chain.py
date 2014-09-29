from sqlalchemy import Column, Integer, String, ForeignKey

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