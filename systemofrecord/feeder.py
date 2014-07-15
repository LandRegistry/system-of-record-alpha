from redis import Redis

class FeederQueue(object):

    def __init__(self, app):
        self.redis_host = app.config.get('REDIS_HOST')
        self.redis_queue = app.config.get('REDIS_QUEUE_KEY')
        self.redis = Redis(self.redis_host)
        self.logger = app.logger # bit quick and dirty


    def enqueue(self, number, json):
        try:
            self.redis.rpush(self.redis_queue, json)
            self.logger .info("Enqueued data for title %s: data: %s" % (number, json))
        except Exception, e:
            self.logger .info(e)
            self.logger .info("Couldn't enqueue data for title %s: data: %s" % (number, json))
