from Crypto.Hash import SHA256
from .utils import load_keys, create_keys
from simplejson import load
from flask import json
from sqlalchemy import Table, Column, MetaData, Integer
from sqlalchemy.dialects.postgresql import JSON
import os
from .server import app
from systemofrecord import db


class DBStore(object):

    def __init__(self, app):
        pass

    def put_last(self, data):
        # TODO check data integrity using public key
        # (or introduce some chain object to handle validation and
        # then just delegate to some storage mechanism for write of file)
        # TODO save data to PostgresQL DB
        title = Titles(data)
        db.session.add(title)
        db.session.commit()

    def get_last(self,):
        # TODO read specific entry
        titles = Titles.query.first()
        return {'title':titles.data}

    def get_title(self, title_number, timestamp):
        # TODO read data from PostgresQL DB
        pass

    def list_titles(self):
        # TODO read data from PostgresQL DB
        pass


class Titles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #data = db.Column('data', JSON)
    data = db.Column('data', db.String(512))

    def __init__(self, data):
        self.data = data


class MemoryStore(object):

    def __init__(self):
        self.store = {}

    def get_last(self):
        return self.store.get('head.json')

    def put_last(self, data):
        key = '%s-%s.json ' % (data['title_number'], data['created_ts'])
        latest_title = 'head.json'
        self.store[key] = data
        self.store[latest_title] = data

    def list_titles(self):
        return [{k.split('/ ')[0]: v}
                for k, v in self.store.iteritems() if 'head' in k]

    def clear(self):
        self.store.clear()
