from flask import logging

from systemofrecord.datatypes import system_of_record_request_validator as validator

from systemofrecord.services import ingest_queue_provider


class IngestQueueProducer(object):
    def __init__(self):
        self.logger = logging.getLogger('commitbuffer.IngestQueue')
        self.logger.addHandler(logging.StreamHandler())
        self.logger.setLevel(logging.INFO)

    def enqueue(self, message):
        try:
            validator.validate(message)
            ingest_queue_provider.add_to_queue(validator.to_canonical_form(message))
        except Exception as e:
            self.logger.error("Could not enqueue message: [message: %s] [exception: %s]" % (message, e))
            # TODO: Store failures somewhere. Possible data loss!
            raise e



