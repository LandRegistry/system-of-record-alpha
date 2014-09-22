import os
import logging
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from raven.contrib.flask import Sentry

app = Flask(__name__)
app.config.from_object(os.environ.get('SETTINGS'))
db = SQLAlchemy(app)

# Sentry exception reporting
if 'SENTRY_DSN' in os.environ:
    sentry = Sentry(app, dsn=os.environ['SENTRY_DSN'])

if not app.debug:
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)

app.logger.info("\nConfiguration\n%s\n" % app.config)

from systemofrecord.health import Health
from systemofrecord.repository import blockchain_repository
from systemofrecord.feeder import FeederQueue

feeder_queue = FeederQueue(app)

Health(app, checks=[blockchain_repository.health, feeder_queue.health])


