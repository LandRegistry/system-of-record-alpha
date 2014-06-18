from Crypto.Hash import SHA256
from .utils import load_keys, create_keys

from flask import json

import boto

class Storage(object,):

    def __init__(self, config):
        self.aws_key = config['AWS_KEY']
        self.aws_secret = config['AWS_SECRET']
        self.s3_bucket = config['S3_BUCKET']

    def put(self, data):

       #TODO check data integrity using public key
       bucket = self.__get_bucket()

       key_path = "%s/%s.json" % (data['title_number'], data['sha256'])
       key = bucket.new_key(key_path)
       key.set_contents_from_string(json.dumps(data), encrypt_key=True)
       self.__set_new_head(data['title_number'], bucket, key_path)

    def get(self, title_number):
        bucket = self.__get_bucket()
        key = '%s/head.json' % title_number
        return bucket.get_key(key)

    def __set_new_head(self, title_number, source_bucket, source_key):
        destination_key  = "%s/%s.json" % (title_number,  'head')
        source_bucket.copy_key(destination_key, source_bucket.name,  source_key)


    def __get_bucket(self):
        connection = boto.connect_s3(self.aws_key, self.aws_secret)
        return connection.get_bucket(self.s3_bucket )
