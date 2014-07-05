from Crypto.Hash import SHA256
from .utils import load_keys, create_keys
from simplejson import load
from flask import json
from flask.ext.sqlalchemy import SQLAlchemy
import os

class DBStore(object):

    def __init__(self, app):

        if 'DATABASE_URL' in os.environ:
            app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL'].replace('postgres://', 'postgresql+psycopg2://')
        else:
            app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://sysofrec:password@%s/sysofrec' % os.environ.get('SYSOFRECDB_1_PORT_5432_TCP', '').replace('tcp://', '')
        db = SQLAlchemy(app)

    def put_last(self, data):
       # TODO check data integrity using public key
       # (or introduce some chain object to handle validation and
       # then just delegate to some storage mechanism for write of file)

       # TODO save data to PostgresQL DB
       pass

    def get_last(self,):
        # TODO read data from PostgresQL DB
        pass

    def get_title(self, title_number, timestamp):
        # TODO read data from PostgresQL DB
        pass

    def list_titles(self):
        # TODO read data from PostgresQL DB
        pass

class MemoryStore(object):

    def __init__(self):
        self.store = {}

    def get_last(self):
        return self.store.get('head.json')

    def put_last(self, data):
        key =  '%s-%s.json ' % (data['title_number'], data['created_ts'])
        latest_title =  'head.json'
        self.store[key] = data
        self.store[latest_title] = data

    def list_titles(self):
        return [{k.split( '/ ')[0] : v} for k,v in self.store.iteritems() if 'head' in k]

    def clear(self):
        self.store.clear()
