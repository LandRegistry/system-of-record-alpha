from flask import logging

from systemofrecord.datatypes import system_of_record_request_validator
from systemofrecord.services import ingest_queue_provider


class IngestQueue(object):
    def __init__(self):
        self.logger = logging.getLogger('commitbuffer.IngestQueue')
        self.logger.addHandler(logging.StreamHandler())
        self.logger.setLevel(logging.INFO)

    def enqueue(self, message):
        try:
            system_of_record_request_validator.validate(message)
            ingest_queue_provider.add_to_queue(system_of_record_request_validator.to_canonical_form(message))
        except Exception as e:
            self.logger.error("Could not enqueue message: [message: %s] [exception: %s]" % (message, e))
            # TODO: Store failures somewhere. Possible data loss!
            raise e



