from systemofrecord.repository import blockchain_object_repository
from systemofrecord.repository.message_id_validator import InvalidTitleIdException
from tests.system_of_record_message_fixtures import valid_message_without_tags, \
    valid_system_of_record_input_message_with_two_tags

from tests.teardown_unittest import TeardownUnittest

test_object_id = valid_message_without_tags['object']['object_id']


class BlockchainObjectRepositoryTestCase(TeardownUnittest):
    def test_can_store_object_data(self):
        blockchain_object_repository.store_object(
            object_id=test_object_id,
            data=valid_message_without_tags)

        loaded_object = blockchain_object_repository.load_object(test_object_id)

        self.check_loaded_object(loaded_object.as_dict())

    def test_can_store_object_with_chains(self):
        blockchain_object_repository.store_object(
            object_id=test_object_id,
            data=valid_system_of_record_input_message_with_two_tags)

        loaded_object = blockchain_object_repository.load_object(test_object_id)

        self.check_loaded_object(loaded_object.as_dict())

        self.check_chains_are_equal(
            loaded_object,
            valid_system_of_record_input_message_with_two_tags['object']['chains'])

    def test_adding_new_object_with_same_id_can_load_most_recent_object(self):
        blockchain_object_repository.store_object(
            object_id=test_object_id,
            data=valid_system_of_record_input_message_with_two_tags)

        loaded_first_object = blockchain_object_repository.load_object(test_object_id)

        blockchain_object_repository.store_object(
            object_id=test_object_id,
            data=valid_system_of_record_input_message_with_two_tags)

        loaded_second_object = blockchain_object_repository.load_object(test_object_id)

        self.assertNotEquals(loaded_first_object.blockchain_index, loaded_second_object.blockchain_index)
        self.assertGreater(loaded_second_object.blockchain_index, loaded_first_object.blockchain_index)



    def test_cannot_store_title_with_title_id_not_matching_json_payload(self):
        self.assertRaises(InvalidTitleIdException, blockchain_object_repository.store_object, "foo",
                          valid_message_without_tags)

    def check_chains_are_equal(self, loaded_data, expected_chains):
        self.assertEqual(len(loaded_data.chains), len(expected_chains))

        for expected_chain in expected_chains:
            found_chain = 0
            for maybe_chain in loaded_data.as_dict()['object']['chains']:
                if (maybe_chain['chain_name'] == expected_chain['chain_name']) and \
                        (maybe_chain['chain_value'] == expected_chain['chain_value']):
                    found_chain = 1

            if not found_chain:
                self.fail("Could not find chain " + repr(expected_chain))


    def check_loaded_object(self, loaded_data):
        self.assertIsNotNone(loaded_data)
        loaded_object_info = loaded_data['object']
        self.assertIsInstance(loaded_object_info['db_id'], int)
        self.assertIsInstance(loaded_object_info['creation_timestamp'], int)
        self.assertIsInstance(loaded_object_info['blockchain_index'], int)
        self.assertEquals(loaded_data['object']['object_id'], test_object_id)