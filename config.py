import os

class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    REDIS_HOST = os.environ.get('REDIS_HOST')
    REDIS_QUEUE = os.environ.get('REDIS_QUEUE')

class DevelopmentConfig(Config):
    DEBUG = True

