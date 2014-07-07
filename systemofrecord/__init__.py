import os
import logging
from flask import Flask
from flask.ext.basicauth import BasicAuth
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')

# auth
if os.environ.get('BASIC_AUTH_USERNAME'):
    app.config['BASIC_AUTH_USERNAME'] = os.environ['BASIC_AUTH_USERNAME']
    app.config['BASIC_AUTH_PASSWORD'] = os.environ['BASIC_AUTH_PASSWORD']
    app.config['BASIC_AUTH_FORCE'] = True
    basic_auth = BasicAuth(app)

if not app.debug:
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)

# DB

# TODO move to config.py
if 'DATABASE_URL' in os.environ:
    db_url = os.environ['DATABASE_URL']
    db_url = db_url.replace('postgres://', 'postgresql+psycopg2://')
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
else:
    template = 'postgresql+psycopg2://sysofrec:password@%s/sysofrec'
    db_host = os.environ.get('SYSOFRECDB_1_PORT_5432_TCP', 'localhost:5432')
    db_host = db_host.replace('tcp://', '')
    app.config['SQLALCHEMY_DATABASE_URI'] = template % db_host


print "SqlAlchemy configured with", app.config['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(app)
