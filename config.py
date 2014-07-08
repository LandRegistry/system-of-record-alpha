import os

# TODO move the PostgresQL env vars here from storage.py
USE_INMEMORY_DB = False
if 'USE_INMEMORY_DB' in os.environ:
    USE_INMEMORY_DB = True

DEBUG = True
