from redis import Redis
import urlparse
from cPickle import dumps

from systemofrecord import app





# This module is a wrapper around Redis for queueing features. If we wish to switch
# queueing provider then we only need to change this wrapper.

class QueueProvider(object):
    def __init__(self):
        redis_url = urlparse.urlparse(app.config.get('REDIS_URL'))

        self.redis_server = Redis(
            host=redis_url.hostname,
            port=redis_url.port,
            password=redis_url.password
        )

    def add_to_queue(self, queue_name, data):
        self.redis_server.rpush(queue_name, dumps(data))

    def read_from_queue(self, queue_name, data):
        pass

    def health(self):
        try:
            self.redis_server.info()
            return True, "Redis"
        except Exception as e:
            self.logger.error("Healthcheck failed [%s]" % e)
            return False, "Redis"
