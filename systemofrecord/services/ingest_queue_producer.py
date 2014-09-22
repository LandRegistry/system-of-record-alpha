from systemofrecord.datatypes import system_of_record_request_validator as validator

from systemofrecord.services import ingest_queue
from systemofrecord.services.configure_logging import configure_logging


class IngestQueueProducer(object):
    def __init__(self):
        self.logger = configure_logging()

    def enqueue(self, message):
        try:
            validator.validate(message)
            ingest_queue.add_to_queue(validator.to_canonical_form(message))
        except Exception as e:
            self.logger.error("Could not enqueue message: [message: %s] [exception: %s]" % (message, e))
            # TODO: Store failures somewhere. Possible data loss!
            raise e



