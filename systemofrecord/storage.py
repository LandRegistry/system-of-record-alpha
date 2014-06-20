from Crypto.Hash import SHA256
from .utils import load_keys, create_keys
from simplejson import load
from flask import json
import boto


class S3Store(object):

    def __init__(self, config):
        self.aws_key = config['AWS_KEY']
        self.aws_secret = config['AWS_SECRET']
        self.s3_bucket = config['S3_BUCKET']

    def put(self, data):

       #TODO check data integrity using public key
       bucket = self.__get_bucket()

       key_path = "%s/%s.json" % (data['title_number'], data['created_ts'])
       key = bucket.new_key(key_path)
       key.set_contents_from_string(json.dumps(data), encrypt_key=True)
       self.__set_new_head(data['title_number'], bucket, key_path)

    def get(self, title_number):
        bucket = self.__get_bucket()
        key = '%s/head.json' % title_number
        return bucket.get_key(key)

    def list_titles(self):
        bucket = self.__get_bucket()
        titles = bucket.list()
        latest_titles = []
        for title in titles:
            if 'head.json' in title.name:
                title = bucket.get_key(title.name)
                title_json = load(title)
                title_number = title_json['title_number']
                latest_titles.append({title_number : title_json})
        return latest_titles

    def __set_new_head(self, title_number, source_bucket, source_key):
        destination_key  = "%s/%s.json" % (title_number,  'head')
        source_bucket.copy_key(destination_key, source_bucket.name,  source_key)

    def __get_bucket(self):
        connection = boto.connect_s3(self.aws_key, self.aws_secret)
        return connection.get_bucket(self.s3_bucket )


class MemoryStore(object):

    def __init__(self):
        self.store = {}

    def put(self, data):
        key = "%s/%s.json" % (data['title_number'], data['created_ts'])
        # create an entry with same data called TITLE_NUMBER/head.json as we have on S3
        # I can see we'll ditch this way of identifying at some point soon
        latest_title = "%s/head.json" % data['title_number']
        self.store[key] = data
        self.store[latest_title] = data

    def get(self, title_number):
        return self.store.get(title_number)

    def list_titles(self):
        print self.store
        return [{k:v} for k,v in self.store.iteritems() if 'head' in k]

    def clear(self):
        self.store.clear()

