from tests.QueueUnittest import QueueUnittest

from systemofrecord.services import ingest_queue
from system_of_record_message_fixtures import valid_system_of_record_input_message

class QueueProviderTestCase(QueueUnittest):
    def test_can_add_and_read_from_queue(self):
        self.assertEqual(ingest_queue.queue_size(), 0)
        self.assertTrue(ingest_queue.is_empty())

        ingest_queue.add_to_queue(valid_system_of_record_input_message)

        self.assertEqual(ingest_queue.queue_size(), 1)
        self.assertFalse(ingest_queue.is_empty())

        message = ingest_queue.read_from_queue()

        self.assertEqual(ingest_queue.queue_size(), 0)
        self.assertTrue(ingest_queue.is_empty())
        self.assertEqual(message, valid_system_of_record_input_message)