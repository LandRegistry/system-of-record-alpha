import calendar
import datetime
from systemofrecord import server, db
import unittest
import json
import mock

test_creation_time = calendar.timegm(datetime.datetime.utcnow().timetuple())
the_past = datetime.datetime.now() - datetime.timedelta(days=30)
some_past_timestamp = calendar.timegm(the_past.timetuple())

class SystemOfRecordTestCase(unittest.TestCase):

    def setUp(self):
        server.app.config['TESTING'] = True
        SQLALCHEMY_DATABASE_URI = "sqlite://"
        server.app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
        db.create_all()
        self.app = server.app.test_client()

    @mock.patch('systemofrecord.feeder.FeederQueue.enqueue')
    @mock.patch('systemofrecord.storage.DBStore.put')
    def test_add_title(self, mock_put, mock_enqueue):
        title_number = "TN1234567"
        data = {"title_number": title_number, "address": "The Hovel, Moletown", "created_ts": test_creation_time}
        self.app.post('/titles/%s' % title_number, data = json.dumps(data), content_type='application/json')

        mock_put.assert_called_with(title_number, data)
        mock_enqueue.assert_called_with(title_number, data)


    # @mock.patch('systemofrecord.feeder.FeederQueue.enqueue')
    # def test_get_last_title(self, mock_enqueue):
    #     title_number = "TN1234567"
    #
    #     #create two records
    #     self.app.post('/titles/ANUMB3R', data=json.dumps({
    #         "title_number": "ANUMB3R",
    #         "address": "The Hovel, Moletown",
    #         "created_ts": some_past_timestamp
    #     }), content_type='application/json')
    #
    #     #add another - this will be last now
    #     self.app.post('/titles/%s' % title_number, data=json.dumps({
    #         "title_number": title_number,
    #         "address": "The Palace, Kings Landing",
    #         "created_ts": test_creation_time
    #     }), content_type='application/json')
    #
    #     # get the last record
    #     response = self.app.get('/titles/last')
    #
    #     self.assertEqual(json.loads(response.data), {
    #         "title_number": title_number,
    #         "address": "The Palace, Kings Landing",
    #         "created_ts": test_creation_time
    #     })


if __name__ == '__main__':
    unittest.main()
