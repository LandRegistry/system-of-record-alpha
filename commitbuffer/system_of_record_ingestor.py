from systemofrecord import configure_logging

from systemofrecord.repository import blockchain_object_repository
from systemofrecord.datatypes import system_of_record_request_validator
from systemofrecord.services import feeder_queue, chain_queue_producer


class SystemOfRecordIngestor(object):
    def __init__(self):
        self.logger = configure_logging(self)

    def ingest(self, message):
        self.logger.info("Attempting to append to blockchain: %s" % str(message))

        try:
            if message is not None:
                system_of_record_request_validator.validate(message)
                object_id = message['object']['object_id']
                blockchain_object_repository.store_object(object_id, message)
                loaded_object_from_head_of_blockchain = blockchain_object_repository.load_most_recent_object_with_id(object_id)

                if loaded_object_from_head_of_blockchain:
                    feeder_queue.add_to_queue(loaded_object_from_head_of_blockchain.as_dict())

                    if len(loaded_object_from_head_of_blockchain.chains) > 0:
                        chain_queue_producer.enqueue_for_object(loaded_object_from_head_of_blockchain.as_dict())

                    self.logger.info("Appended object %s to blockchain" % object_id)
                else:
                    self.logger.error(
                        "Could not load object with object_id %s, not enqueueing message %s" % (object_id, message))
            else:
                self.logger.warn("Attempted to ingest null message")
        except Exception as e:
            self.logger.error("Exception caught attempting to append item %s to blockchain" % message, e)
            raise e