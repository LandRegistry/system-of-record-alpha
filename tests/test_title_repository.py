from systemofrecord.repository import InvalidTitleIdException, BlockchainObjectRepository
from tests.system_of_record_message_fixtures import valid_message_without_tags

from tests.teardown_unittest import TeardownUnittest

test_object_id = valid_message_without_tags['object']['object_id']
title_repository = BlockchainObjectRepository()


class TitleRepositoryTestCase(TeardownUnittest):
    def test_can_store_object_data(self):
        title_repository.store_object(object_id=test_object_id, data=valid_message_without_tags)
        loaded_data = title_repository.load_object(test_object_id)

        self.assertIsNotNone(loaded_data)
        loaded_object_info = loaded_data['object_info']
        self.assertIsInstance(loaded_object_info['db_id'], int)
        self.assertIsInstance(loaded_object_info['creation_timestamp'], int)
        self.assertIsInstance(loaded_object_info['blockchain_index'], int)
        self.assertEquals(loaded_data['object']['object_id'], test_object_id)

    def test_cannot_store_title_with_title_id_not_matching_json_payload(self):
        self.assertRaises(InvalidTitleIdException, title_repository.store_object, "foo", valid_message_without_tags)

