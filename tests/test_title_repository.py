from systemofrecord.repository import InvalidTitleIdException, BlockchainObjectRepository

from tests.teardown_unittest import TeardownUnittest
from fixtures import data_from_mint, object_id_1


title_repository = BlockchainObjectRepository()


class TitleRepositoryTestCase(TeardownUnittest):
    def test_can_store_title_data(self):
        title_repository.store_object(object_id=object_id_1, data=data_from_mint)
        loaded_data = title_repository.load_object(object_id_1)

        self.assertIsNotNone(loaded_data)
        loaded_title = loaded_data['title']
        self.assertIsInstance(loaded_title['db_id'], int)
        self.assertIsInstance(loaded_title['creation_timestamp'], int)
        self.assertIsInstance(loaded_title['blockchain_index'], int)
        title_data = loaded_title['data']
        self.assertEquals(loaded_title['title_number'], title_data['title_number'])

    def test_cannot_store_title_with_title_id_not_matching_json_payload(self):
        self.assertRaises(InvalidTitleIdException, title_repository.store_object, "foo", data_from_mint)

