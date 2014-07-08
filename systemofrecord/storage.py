from Crypto.Hash import SHA256
from .utils import load_keys, create_keys
from simplejson import load
from flask import json
from sqlalchemy import Table, Column, MetaData, Integer
from sqlalchemy.dialects.postgresql import JSON
import os
from .server import app
from systemofrecord import db
from systemofrecord.models import Titles


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
        app.logger.info('FOUND SOMETHINGININININININ')
        if titles:
            return {'title': {
                'number':titles.title_number,
                'data':titles.data
            }}
        return []

    def get(self, title_number):
        title = Titles.query.filter_by(title_number=title_number).first()
        if title:
            app.logger.info("Found title %s" % title)
            return {
                'title': {
                    'number':   title.title_number,
                    'data': title.data
            }}
        return None

    def list_titles(self):
        # TODO read data from PostgresQL DB
        return []

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
