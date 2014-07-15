import os

class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    REDIS_HOST = os.environ.get('REDIS_HOST')
    REDIS_QUEUE_KEY = os.environ.get('REDIS_QUEUE_KEY')

class DevelopmentConfig(Config):
    DEBUG = True

class TestConfig(DevelopmentConfig):
        REDIS_HOST = 'redis://user:@localhost:6379'


