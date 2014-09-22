import os


class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    REDIS_URL = os.environ['REDIS_URL']
    REDIS_QUEUE_KEY = os.environ['REDIS_QUEUE_KEY']
    INGEST_QUEUE_NAME = os.environ['INGEST_QUEUE_NAME']


class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(DevelopmentConfig):
    TESTING = True
    DEBUG = True

