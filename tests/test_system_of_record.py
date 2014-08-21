import unittest
import json
import mock

from systemofrecord import server

from data import data_from_mint
from data import title_number

data_for_the_feeder = data_from_mint['title']

class SystemOfRecordTestCase(unittest.TestCase):

    def setUp(self):
        self.app = server.app.test_client()

    @mock.patch("systemofrecord.feeder.FeederQueue.enqueue")
    @mock.patch("systemofrecord.storage.DBStore.put")
    def test_add_title_should_put_to_db_and_queue_data(self, mock_put, mock_enqueue):
        self.app.put("/titles/%s" % title_number, data = json.dumps(data_from_mint), content_type="application/json")
        mock_put.assert_called_with(title_number, data_from_mint)
        mock_enqueue.assert_called_with(title_number, data_for_the_feeder)

    @mock.patch("systemofrecord.storage.DBStore.count")
    @mock.patch("redis.Redis.info")
    def test_health_returns_200(self, mock_redis, mock_db):
        response = self.app.get('/health')
        assert response.status == '200 OK'

    @mock.patch("systemofrecord.storage.DBStore.get")
    def test_get_known_title_gets_from_db(self, mock_db_get):
        self.app.get("/titles/%s" % title_number)
        mock_db_get.assert_called_with(title_number)


    @mock.patch("systemofrecord.storage.DBStore.get", return_value=None)
    def test_get_returns_404_if_title_not_found(self, mock_db_get):
        response = self.app.get("/titles/%s" % title_number)
        mock_db_get.assert_called_with(title_number)
        assert response.status_code == 404
