from flask import make_response

from systemofrecord import storage, feeder_queue
from systemofrecord.services.configure_logging import configure_logging


class StoreObjectController(object):
    def __init__(self):
        self.logger = configure_logging(self)

    def store_object(self, title_number, title_as_json):
        storage.store_object(title_number, title_as_json)
        self.logger.info("Put title json %s on feeder queue" % title_as_json['title'])
        feeder_queue.enqueue(title_number, title_as_json['title'])
        return make_response('OK', 201)