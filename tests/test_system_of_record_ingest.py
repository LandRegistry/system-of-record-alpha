from unittest import TestCase

from commitbuffer import system_of_record_ingestor
from systemofrecord.repository import blockchain_repository
from system_of_record_message_fixtures import valid_message_without_tags, remove_generated_fields_from_loaded_object

test_object_id = valid_message_without_tags['object']['object_id']


class SystemOfRecordIngestTestCase(TestCase):
    def test_can_ingest_well_formed_record(self):
        self.maxDiff = 1024
        self.assertEqual(blockchain_repository.count(), 0)

        system_of_record_ingestor.ingest(valid_message_without_tags)

        self.assertEqual(blockchain_repository.count(), 1)
        self.assertEqual(remove_generated_fields_from_loaded_object(blockchain_repository.load_object(test_object_id)),
                         valid_message_without_tags)