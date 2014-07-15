from redis import Redis
import urlparse

class FeederQueue(object):

    def __init__(self, app):
        self.logger = app.logger # bit quick and dirty
        url = urlparse.urlparse(app.config.get('REDIS_HOST'))
        self.redis_queue = app.config.get('REDIS_QUEUE_KEY')
        self.redis = Redis(host=url.hostname, port=url.port, password=url.password)

    def enqueue(self, number, json):
        try:
            self.redis.rpush(self.redis_queue, json)
            self.logger .info("Enqueued data for title %s: data: %s" % (number, json))
            self.logger.info("Redis: %s" % self.redis)
        except Exception, e:
            self.logger .info(e)
            self.logger .info("Couldn't enqueue data for title %s: data: %s" % (number, json))
