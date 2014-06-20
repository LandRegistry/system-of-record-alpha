import calendar
import datetime
from systemofrecord import server
from systemofrecord.storage import MemoryStore, S3Store
import unittest
import json

test_creation_time = calendar.timegm(datetime.datetime.utcnow().timetuple())


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
        self.app.post('/titles', data=json.dumps(
            {
                "title_number": "TN1234567",
                "address": "The Hovel, Moletown",
                "created_ts": test_creation_time
            }), content_type='application/json')

        response = self.app.get('/titles')

        print type(json.loads(response.data))

        title_number_id = "TN1234567/head.json"

        self.assertEqual(json.loads(response.data), {
            'titles': [
                        {
                            title_number_id : {
                                "title_number": "TN1234567",
                                "address": "The Hovel, Moletown",
                                "created_ts": test_creation_time
                            }
                        }
                    ]
            })


if __name__ == '__main__':
    unittest.main()
