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

    def as_dict(self):
        return {
            'chain_name': self.name,
            'chain_value': self.value
        }

    def __repr__(self):
        return repr(self.as_dict())