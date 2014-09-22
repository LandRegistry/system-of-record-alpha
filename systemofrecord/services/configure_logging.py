from flask import logging

from systemofrecord.server import app


def configure_logging(obj):
    logger = logging.getLogger(obj.__class__.__name__)
    logger.addHandler(logging.StreamHandler())

    if app.config['DEBUG']:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    return logger