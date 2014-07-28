import unittest
import json

from systemofrecord import db
from systemofrecord.server import DBStore
from systemofrecord.models import Title

from data import data_from_mint
from data import title_number

class StorageTestCase(unittest.TestCase):

    def setUp(self):
        db.create_all()
        self.storage = DBStore()

    def test_put_with_payload_creates_title(self):
        self.storage.put(title_number, data_from_mint)
        #bypass db store api and check db
        title = Title.query.filter_by(title_number=title_number).first()
        assert title
        assert title.title_number == title_number

    # need to change data type on data column to json
    # then can change this test to check data
    # but then tests would need postgres running ...
    # then this changes to integration test?
    def test_get_title_with_number_returns_title(self):
        self.storage.put(title_number, data_from_mint)
        returned_data = self.storage.get(title_number)
        assert returned_data
        assert returned_data['title']['number'] == title_number
