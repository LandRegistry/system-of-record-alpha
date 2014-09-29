from datatypes.exceptions import DataDoesNotMatchSchemaException

from commitbuffer import blockchain_ingestor
from systemofrecord.repository import blockchain_object_repository
from systemofrecord.services import feeder_queue, tag_queue
from system_of_record_message_fixtures import *
from tests.teardown_unittest import TeardownUnittest


test_object_id = valid_message_without_tags['object']['object_id']


class SystemOfRecordIngestTestCase(TeardownUnittest):
    def test_can_ingest_well_formed_record_without_tags(self):
        self.check_system_is_empty()

        blockchain_ingestor.ingest(valid_message_without_tags)

        self.check_feeder_queue_and_database_contains_a_number_of_messages(1)
        self.check_tag_queue_is_empty()

        loaded_object = blockchain_object_repository.load_object(test_object_id)

        # Check the loaded object looks like the one that we ingested
        self.assertEquals(loaded_object['object']['data'], valid_message_without_tags['object']['data'])
        self.assertEquals(loaded_object['object']['object_id'], valid_message_without_tags['object']['object_id'])

        # Ingest another message without tags
        blockchain_ingestor.ingest(valid_message_without_tags)

        self.check_feeder_queue_and_database_contains_a_number_of_messages(2)
        self.check_tag_queue_is_empty()

    def test_can_ingest_well_formed_message_with_tags(self):
        self.check_system_is_empty()

        # Ingest a message with 2 tags.
        blockchain_ingestor.ingest(valid_system_of_record_input_message_with_two_tags)

        # However, as the system was empty we're not expecting any tag messages, only the feeder queue message
        self.check_feeder_queue_and_database_contains_a_number_of_messages(1)
        # TODO Check tags are in database....

        self.check_tag_queue_contains_a_number_of_messages(0)

        # Now we'll add a new message with the same 2 tags
        blockchain_ingestor.ingest(valid_system_of_record_input_message_with_two_tags)

        # Now, we're expecting 2 items on the feeder queue & db
        self.check_feeder_queue_and_database_contains_a_number_of_messages(2)
        # And we're expecting 1 item on the tag queue
        self.check_tag_queue_contains_a_number_of_messages(1)

    def test_cant_ingest_bad_record(self):
        self.check_system_is_empty()

        self.assertRaises(DataDoesNotMatchSchemaException, blockchain_ingestor.ingest,
                          invalid_message_with_extra_keys)
        self.assertRaises(DataDoesNotMatchSchemaException, blockchain_ingestor.ingest,
                          invalid_message_without_object)
        self.assertRaises(DataDoesNotMatchSchemaException, blockchain_ingestor.ingest,
                          invalid_message_without_schema_version)

        self.check_feeder_queue_and_database_contains_a_number_of_messages(0)


    def test_can_ingest_none(self):
        self.check_system_is_empty()

        blockchain_ingestor.ingest(None)

        self.check_system_is_empty()

    def check_system_is_empty(self):
        self.check_feeder_queue_and_database_contains_a_number_of_messages(0)
        self.check_tag_queue_contains_a_number_of_messages(0)

    def check_tag_queue_is_empty(self):
        self.check_tag_queue_contains_a_number_of_messages(0)

    def check_tag_queue_contains_a_number_of_messages(self, number_of_messages):
        self.assertEqual(tag_queue.queue_size(), number_of_messages)

    def check_feeder_queue_and_database_contains_a_number_of_messages(self, number_of_messages):
        self.assertEqual(blockchain_object_repository.count(), number_of_messages)
        self.assertEqual(feeder_queue.queue_size(), number_of_messages)