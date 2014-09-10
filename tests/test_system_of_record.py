import unittest
import json
import mock

from systemofrecord import server
from systemofrecord.models import Title
from data import data_from_mint
from data import title_id


data_for_the_feeder = data_from_mint['title']


class SystemOfRecordTestCase(unittest.TestCase):
    def setUp(self):
        self.app = server.app.test_client()

    def tearDown(self):
        Title.query.delete()

    @mock.patch("systemofrecord.feeder.FeederQueue.enqueue")
    def test_add_title_should_put_to_db_and_queue_data(self, mock_enqueue):
        self.app.put("/titles/%s" % title_id, data=json.dumps(data_from_mint), content_type="application/json")
        mock_enqueue.assert_called_with(title_id, data_for_the_feeder)

    @mock.patch("redis.Redis.info")
    def test_health_returns_200(self, mock_redis):
        response = self.app.get('/health')
        assert response.status == '200 OK'

    def test_get_known_title_gets_from_db(self):
        self.app.get("/titles/%s" % title_id)
        # mock_db_get.assert_called_with(title_number)

    def test_get_returns_404_if_title_not_found(self):
        response = self.app.get("/titles/%s" % title_id)
        # mock_db_get.assert_called_with(title_id)
        assert response.status_code == 404
