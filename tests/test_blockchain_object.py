from systemofrecord.repository import blockchain_object_repository
from systemofrecord.repository.message_id_validator import InvalidTitleIdException
from tests.system_of_record_message_fixtures import valid_message_without_tags, \
    valid_system_of_record_input_message_with_two_tags

from tests.teardown_unittest import TeardownUnittest

test_object_id = valid_message_without_tags['object']['object_id']


class BlockchainObjectRepositoryTestCase(TeardownUnittest):
    def test_can_store_object_data(self):
        blockchain_object_repository.store_object(object_id=test_object_id, data=valid_message_without_tags)
        loaded_object = blockchain_object_repository.load_object(test_object_id)

        self.check_loaded_object(loaded_object.as_dict())

    def test_can_store_object_with_chains(self):
        blockchain_object_repository.store_object(object_id=test_object_id,
                                                  data=valid_system_of_record_input_message_with_two_tags)
        loaded_object = blockchain_object_repository.load_object(test_object_id)

        self.check_loaded_object(loaded_object.as_dict())

        self.assertEqual(len(loaded_object.chains), 2)

    def test_cannot_store_title_with_title_id_not_matching_json_payload(self):
        self.assertRaises(InvalidTitleIdException, blockchain_object_repository.store_object, "foo",
                          valid_message_without_tags)

    def check_loaded_object(self, loaded_data):
        self.assertIsNotNone(loaded_data)
        loaded_object_info = loaded_data['object']
        self.assertIsInstance(loaded_object_info['db_id'], int)
        self.assertIsInstance(loaded_object_info['creation_timestamp'], int)
        self.assertIsInstance(loaded_object_info['blockchain_index'], int)
        self.assertEquals(loaded_data['object']['object_id'], test_object_id)