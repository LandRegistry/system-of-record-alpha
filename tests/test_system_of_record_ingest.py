from commitbuffer import system_of_record_ingestor
from systemofrecord.repository import blockchain_repository
from system_of_record_message_fixtures import *
from tests.teardown_unittest import TeardownUnittest
from datatypes.exceptions import DataDoesNotMatchSchemaException

test_object_id = valid_message_without_tags['object']['object_id']


class SystemOfRecordIngestTestCase(TeardownUnittest):
    def test_can_ingest_well_formed_record(self):
        self.assertEqual(blockchain_repository.count(), 0)

        system_of_record_ingestor.ingest(valid_message_without_tags)

        self.assertEqual(blockchain_repository.count(), 1)
        self.assertEqual(remove_generated_fields_from_loaded_object(blockchain_repository.load_object(test_object_id)),
                         valid_message_without_tags)

        system_of_record_ingestor.ingest(valid_message_without_tags)

        self.assertEqual(blockchain_repository.count(), 2)

    def test_cant_ingest_bad_record(self):
        self.assertEqual(blockchain_repository.count(), 0)

        self.assertRaises(DataDoesNotMatchSchemaException, system_of_record_ingestor.ingest,
                          invalid_message_with_extra_keys)
        self.assertRaises(DataDoesNotMatchSchemaException, system_of_record_ingestor.ingest,
                          invalid_message_without_object)
        self.assertRaises(DataDoesNotMatchSchemaException, system_of_record_ingestor.ingest,
                          invalid_message_without_schema_version)

        self.assertEqual(blockchain_repository.count(), 0)

    def test_can_ingest_none(self):
        self.assertEqual(blockchain_repository.count(), 0)

        system_of_record_ingestor.ingest(None)
        self.assertEqual(blockchain_repository.count(), 0)
