from datatypes.exceptions import DataDoesNotMatchSchemaException

from commitbuffer import blockchain_ingestor
from systemofrecord.repository import blockchain_repository
from systemofrecord.services import feeder_queue
from system_of_record_message_fixtures import *
from tests.teardown_unittest import TeardownUnittest


test_object_id = valid_message_without_tags['object']['object_id']


class SystemOfRecordIngestTestCase(TeardownUnittest):
    def test_can_ingest_well_formed_record(self):
        self.assertEqual(blockchain_repository.count(), 0)
        self.assertEqual(feeder_queue.queue_size(), 0)

        blockchain_ingestor.ingest(valid_message_without_tags)

        self.assertEqual(blockchain_repository.count(), 1)
        self.assertEqual(feeder_queue.queue_size(), 1)
        loaded_object = blockchain_repository.load_object(test_object_id)

        self.assertEquals(loaded_object['object']['data'], valid_message_without_tags['object']['data'])
        self.assertEquals(loaded_object['object']['object_id'], valid_message_without_tags['object']['object_id'])

        blockchain_ingestor.ingest(valid_message_without_tags)

        self.assertEqual(blockchain_repository.count(), 2)
        self.assertEqual(feeder_queue.queue_size(), 2)


    def test_cant_ingest_bad_record(self):
        self.assertEqual(blockchain_repository.count(), 0)
        self.assertEqual(feeder_queue.queue_size(), 0)

        self.assertRaises(DataDoesNotMatchSchemaException, blockchain_ingestor.ingest,
                          invalid_message_with_extra_keys)
        self.assertRaises(DataDoesNotMatchSchemaException, blockchain_ingestor.ingest,
                          invalid_message_without_object)
        self.assertRaises(DataDoesNotMatchSchemaException, blockchain_ingestor.ingest,
                          invalid_message_without_schema_version)

        self.assertEqual(blockchain_repository.count(), 0)
        self.assertEqual(feeder_queue.queue_size(), 0)


    def test_can_ingest_none(self):
        self.assertEqual(blockchain_repository.count(), 0)
        self.assertEqual(feeder_queue.queue_size(), 0)

        blockchain_ingestor.ingest(None)
        self.assertEqual(blockchain_repository.count(), 0)
        self.assertEqual(feeder_queue.queue_size(), 0)
