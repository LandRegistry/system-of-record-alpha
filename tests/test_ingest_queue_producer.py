from tests.QueueUnittest import QueueUnittest

from systemofrecord.services import ingest_queue_producer, ingest_queue
from system_of_record_message_fixtures import valid_message_without_tags


class TestIngestQueueProducer(QueueUnittest):
    def test_can_append_items_to_queue(self):
        self.assertEqual(ingest_queue.queue_size(), 0)
        ingest_queue_producer.enqueue(valid_message_without_tags)
        ingest_queue_producer.enqueue(valid_message_without_tags)
        self.assertEqual(ingest_queue.queue_size(), 2)