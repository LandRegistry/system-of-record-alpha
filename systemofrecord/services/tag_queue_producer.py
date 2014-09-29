from systemofrecord import configure_logging
from systemofrecord.services import tag_queue
from systemofrecord.datatypes import system_of_record_tag_message_validator as validator


class TagQueueProducer(object):
    def __init__(self):
        self.logger = configure_logging(self)

    def enqueue(self, message):
        try:
            validator.validate(message)
            tag_queue.add_to_queue(message)
        except Exception as e:
            self.logger.error("Could not enqueue message: [message: %s] [exception: %s]" % (message, e))
            raise e
