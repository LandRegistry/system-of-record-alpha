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
            json_ascii = convert_to_ascii(json)
            self.redis.rpush(self.redis_queue, json_ascii)
            self.logger .info("Enqueued data for title %s: data: %s" % (number, json))
            self.logger.info("Redis: %s" % self.redis)
        except Exception, e:
            self.logger .info(e)
            self.logger .info("Couldn't enqueue data for title %s: data: %s" % (number, json))


def convert_to_ascii(input):
    if isinstance(input, dict):
        return {convert_to_ascii(key): convert_to_ascii(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert_to_ascii(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
