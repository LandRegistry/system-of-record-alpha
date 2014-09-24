import os


class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    REDIS_URL = os.environ['REDIS_URL']
    FEEDER_QUEUE_NAME = os.environ['FEEDER_QUEUE_NAME']
    INGEST_QUEUE_NAME = os.environ['INGEST_QUEUE_NAME']
    INGEST_QUEUE_POLL_INTERVAL_IN_SECONDS = float(os.environ['INGEST_QUEUE_POLL_INTERVAL_IN_SECONDS'])


class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(DevelopmentConfig):
    TESTING = True
    DEBUG = True

