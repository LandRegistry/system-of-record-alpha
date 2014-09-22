from systemofrecord.services.configure_logging import configure_logging

from systemofrecord.repository import blockchain_repository
from systemofrecord.datatypes import system_of_record_request_validator
from datatypes.exceptions import DataDoesNotMatchSchemaException


class SystemOfRecordIngestor(object):
    def __init__(self):
        self.logger = configure_logging(self)

    def ingest(self, message):
        try:
            if message:
                system_of_record_request_validator.validate(message)
                blockchain_repository.store_object(message['object']['object_id'], message)
            else:
                self.logger.error("Attempted to ingest null message!")
        except DataDoesNotMatchSchemaException as e:
            self.logger.error("Could not validate message: %s error %s") % (repr(message), repr(e))
            raise e