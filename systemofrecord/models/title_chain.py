from sqlalchemy import Column, Integer, String
from systemofrecord import db


class TitleChain(db.Model):
    __tablename__ = 'title_chain'

    title_id = Column(String(64))

