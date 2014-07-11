import os
import logging
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ.get('SETTINGS'))


if not app.debug:
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)

app.logger.info( "============")
app.logger.info(app.config)
app.logger.info("============")

db = SQLAlchemy(app)
