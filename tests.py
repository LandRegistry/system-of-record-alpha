import calendar
import datetime
from systemofrecord import server
from systemofrecord.storage import MemoryStore, S3Store
import unittest
import json

test_creation_time = calendar.timegm(datetime.datetime.utcnow().timetuple())
the_past = datetime.datetime.now() - datetime.timedelta(days=30)
some_past_timestamp = calendar.timegm(the_past.timetuple())

class SystemOfRecordTestCase(unittest.TestCase):

    def setUp(self):

        server.app.config['TESTING'] = True
        self.app = server.app.test_client()
        #make sure we're running against in memory store
        if type(server.storage) == S3Store:
            server.storage = MemoryStore()
            print "S3 was used, switched to memory store"

    def tearDown(self):
        server.storage.clear()

    def test_empty_store(self):
        response = self.app.get('/titles')
        self.assertEqual(json.loads(response.data),  {'titles': []})

    def test_add_title(self):
        title_number = "TN1234567"
        self.app.post('/titles', data=json.dumps(
            {
                "title_number": title_number,
                "address": "The Hovel, Moletown",
                "created_ts": test_creation_time
            }), content_type='application/json')

        response = self.app.get('/titles')

        self.assertEqual(json.loads(response.data), {
            'titles': [
                        {
                            title_number : {
                                "title_number": "TN1234567",
                                "address": "The Hovel, Moletown",
                                "created_ts": test_creation_time
                            }
                        }
                    ]
            })

    def test_get_latest_title(self):
        title_number = "TN1234567"

        self.app.post('/titles', data=json.dumps(
            {
                "title_number": title_number,
                "address": "The Hovel, Moletown",
                "created_ts": test_creation_time
            }), content_type='application/json')

        latest_url = '/titles/%s' % "TN1234567"
        response = self.app.get(latest_url)

        self.assertEqual(json.loads(response.data), {
                        title_number : {
                            "title_number": "TN1234567",
                            "address": "The Hovel, Moletown",
                            "created_ts": test_creation_time
                        }
            })

    def test_get_title_by_full_id(self):
        title_number = "TN1234567"

        #create two records
        self.app.post('/titles', data=json.dumps(
            {
                "title_number": title_number,
                "address": "The Hovel, Moletown",
                "created_ts": some_past_timestamp
            }), content_type='application/json')


        #update to now'ish
        self.app.post('/titles', data=json.dumps(
            {
                "title_number": title_number,
                "address": "The Hovel, Moletown, Up North",
                "created_ts": test_creation_time
            }), content_type='application/json')


        # get the old one
        title_with_timestamp = "%s/%d" % (title_number, some_past_timestamp)
        url_with_id = '/titles/%s' % title_with_timestamp
        response = self.app.get(url_with_id)

        self.assertEqual(json.loads(response.data), {
                        title_number : {
                            "title_number": "TN1234567",
                            "address": "The Hovel, Moletown",
                            "created_ts": some_past_timestamp
                        }
                    }
            )

        # get the latest
        url_for_latest = '/titles/%s' % title_number
        response = self.app.get(url_for_latest)

        self.assertEqual(json.loads(response.data), {
                        title_number : {
                            "title_number": "TN1234567",
                            "address": "The Hovel, Moletown, Up North",
                            "created_ts": test_creation_time
                        }
                    }
            )



if __name__ == '__main__':
    unittest.main()
