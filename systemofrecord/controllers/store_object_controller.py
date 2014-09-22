from flask import make_response

from systemofrecord.services.configure_logging import configure_logging
from systemofrecord.repository import blockchain_repository
from systemofrecord import feeder_queue


class StoreObjectController(object):
    def __init__(self):
        self.logger = configure_logging(self)

    def store_object(self, object_id, object):
        blockchain_repository.store_object(object_id, object)
        self.logger.info("Put title json %s on feeder queue" % object['object']['object_id'])
        feeder_queue.enqueue(object_id, object)
        return make_response('OK', 201)