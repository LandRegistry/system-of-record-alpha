from systemofrecord import configure_logging

from systemofrecord.repository import blockchain_repository
from systemofrecord.datatypes import system_of_record_request_validator
from systemofrecord import feeder_queue
from datatypes.exceptions import DataDoesNotMatchSchemaException


class SystemOfRecordIngestor(object):
    def __init__(self):
        self.logger = configure_logging(self)

    def ingest(self, message):
        self.logger.info("Appending to blockchain: %s" % str(message))

        try:
            if message is not None:
                system_of_record_request_validator.validate(message)
                object_id = message['object']['object_id']
                blockchain_repository.store_object(object_id, message)
                feeder_queue.enqueue(object_id, message)
            else:
                self.logger.error("Attempted to ingest null message: " + repr(message))
        except DataDoesNotMatchSchemaException as e:
            self.logger.error("Could not validate message: %s error: %s" % (repr(message), repr(e)))
            raise e