import json
import mock

from fixtures import data_from_mint

from fixtures import title_id
from tests.teardown_unittest import TeardownUnittest


data_for_the_feeder = data_from_mint['title']


class SystemOfRecordTestCase(TeardownUnittest):
    @mock.patch("systemofrecord.feeder.FeederQueue.enqueue")
    def test_add_title_should_put_to_db_and_queue_data(self, mock_enqueue):
        self.app.put("/titles/%s" % title_id, data=json.dumps(data_from_mint), content_type="application/json")

        mock_enqueue.assert_called_with(title_id, data_for_the_feeder)

    @mock.patch("redis.Redis.info")
    def test_health_returns_200(self, mock_redis):
        response = self.app.get('/health')
        self.assertEqual(response.status, '200 OK')

    def test_get_known_title_gets_from_db(self):
        self.app.put("/titles/%s" % title_id, data=json.dumps(data_from_mint), content_type="application/json")
        self.app.get("/titles/%s" % title_id)

    def test_get_returns_404_if_title_not_found(self):
        response = self.app.get("/titles/%s" % title_id)
        self.assertEqual(response.status_code, 404)
