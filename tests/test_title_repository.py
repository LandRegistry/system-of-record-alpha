import simplejson
from systemofrecord.repository import DBStore
from tests.teardown_unittest import TeardownUnittest

from fixtures import data_from_mint, title_id


class TitleRepositoryTestCase(TeardownUnittest):
    def setUp(self):
        super(TitleRepositoryTestCase, self).setUp()
        self.title_repository = DBStore()

    def test_can_store_title_data(self):
        self.title_repository.put(title_number=title_id, data=data_from_mint)
        loaded_data = self.title_repository.get(title_id)

        self.assertIsNotNone(loaded_data)
        loaded_title = loaded_data['title']
        self.assertIsInstance(loaded_title['db_id'], int)
        self.assertIsInstance(loaded_title['creation_timestamp'], int)
        self.assertIsInstance(loaded_title['blockchain_index'], int)
        title_data = simplejson.loads(loaded_title['data'])
        self.assertEquals(loaded_title['title_number'], title_data['title_number'])
        

