from unittest import TestCase

from systemofrecord.services import ingest_queue
from system_of_record_message_fixtures import valid_message_without_tags


class IngestQueueConsumerTestCase(TestCase):
    def test_can_consume_queue_of_messages(self):
        ingest_queue.add_to_queue(valid_message_without_tags)
        ingest_queue.add_to_queue(valid_message_without_tags)

