from systemofrecord import configure_logging
from systemofrecord.services import chain_queue


class ChainQueueProducer(object):
    def __init__(self):
        self.logger = configure_logging(self)

    def enqueue_for_object(self, blockchain_object):
        try:
            chain_queue.add_to_queue(self.create_chain_message(blockchain_object))
        except Exception as e:
            self.logger.error("Could not enqueue chain messages for object: %s exception: %s" % (
                repr(blockchain_object.as_dict()), e))
            raise e

    def create_chain_message(self, blockchain_object):
        pass