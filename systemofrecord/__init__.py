import os
import logging
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from raven.contrib.flask import Sentry

from systemofrecord.health import Health


app = Flask(__name__)
app.config.from_object(os.environ.get('SETTINGS'))

# Sentry exception reporting
if 'SENTRY_DSN' in os.environ:
    sentry = Sentry(app, dsn=os.environ['SENTRY_DSN'])

if not app.debug:
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)

app.logger.info("\nConfiguration\n%s\n" % app.config)

db = SQLAlchemy(app)

# We need to import these after 'db' to avoid circular imports
from systemofrecord.feeder import FeederQueue
from systemofrecord.repository import DBStore

feeder_queue = FeederQueue(app)
storage = DBStore()
Health(app, checks=[storage.health, feeder_queue.health])


