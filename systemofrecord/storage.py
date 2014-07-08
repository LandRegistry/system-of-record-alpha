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

    def put(self, title_number, data):
        # TODO check data integrity using public key
        # (or introduce some chain object to handle validation and
        # then just delegate to some storage mechanism for write of file)
        # TODO save data to PostgresQL DB
        title = Titles(title_number, str(data))
        db.session.add(title)
        db.session.commit()

    def get_last(self,):
        titles = Titles.query.first()
        return {'title': {
            'number':titles.title_number,
            'data':titles.data
        }}

    def get(self, title_number):
        titles = Titles.query.filter_by(title_number=title_number).first()
        return {'title': {
            'number':titles.title_number,
            'data':titles.data
        }}

    def list_titles(self):
        # TODO read data from PostgresQL DB
        pass


class Titles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title_number = db.Column('title_number', db.String(64))
    #data = db.Column('data', JSON)
    data = db.Column('data', db.String(512))

    def __init__(self, title_number, data):
        self.title_number = title_number
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
