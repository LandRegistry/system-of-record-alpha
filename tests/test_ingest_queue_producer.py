from tests.queue_unittest import QueueUnittest

from systemofrecord.services import ingest_queue_producer, ingest_queue
from system_of_record_message_fixtures import valid_message_without_tags, invalid_message_without_object
from datatypes.exceptions import DataDoesNotMatchSchemaException


class TestIngestQueueProducer(QueueUnittest):
    def test_can_append_items_to_queue(self):
        self.assertEqual(ingest_queue.queue_size(), 0)
        ingest_queue_producer.enqueue(valid_message_without_tags)
        ingest_queue_producer.enqueue(valid_message_without_tags)
        self.assertEqual(ingest_queue.queue_size(), 2)


    def test_cannot_add_invalid_messages_to_queue(self):
        self.assertEqual(ingest_queue.queue_size(), 0)
        self.assertRaises(DataDoesNotMatchSchemaException, ingest_queue_producer.enqueue,
                          invalid_message_without_object)
        self.assertEqual(ingest_queue.queue_size(), 0)
