from redis import Redis

import urlparse
import cPickle as pickle
import logging

class FeederQueue(object):

    def __init__(self, app):
        self.redis_url = urlparse.urlparse(app.config.get('REDIS_URL'))
        self.redis_queue_key = app.config.get('REDIS_QUEUE_KEY')
        self.redis = None
        self.logger = logging.getLogger('systemofrecord.feeder.FeederQueue')
        self.logger.addHandler(logging.StreamHandler())
        self.logger.setLevel(logging.INFO)

    def enqueue(self, number, json):
        try:
            queue = self.__get_queue()
            json_pickle = pickle.dumps(json)
            queue.rpush(self.redis_queue_key, json_pickle)
            self.logger.info("Enqueued data for title %s: data: %s" % (number, json))
        except pickle.PicklingError as e:
            self.logger.error(e)
            self.logger.error("Couldn't pickle data for title %s: data: %s" % (number, json))
        except Exception as e:
            self.logger.error(e)
            self.logger.error("Could not enqueue data for title %s: data: %s" % (number, json))

    def __get_queue(self):
        if not self.redis:
            self.redis = Redis(host=self.redis_url.hostname, port= self.redis_url.port, password= self.redis_url.password)
        return self.redis


