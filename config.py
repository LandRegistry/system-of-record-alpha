import os


class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    REDIS_URL = os.environ['REDIS_URL']
    REDIS_QUEUE_KEY = os.environ['REDIS_QUEUE_KEY']


class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(DevelopmentConfig):
    TESTING = True
    DEBUG = True


class DockerConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SYSOFRECDB_1_PORT_5432_TCP', '').replace('tcp://',
                                                                                       'postgresql://docker:docker@') + '/docker'
    REDIS_URL = os.environ.get('REDIS_1_PORT_6379_TCP', '').replace('tcp://', 'http://')

