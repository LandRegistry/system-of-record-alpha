import calendar
import datetime
from systemofrecord import server, db
import unittest
import json
import mock

test_creation_time = calendar.timegm(datetime.datetime.utcnow().timetuple())
the_past = datetime.datetime.now() - datetime.timedelta(days=30)
some_past_timestamp = calendar.timegm(the_past.timetuple())

title_number = "AB1234567"
data_from_mint = {
        "public_key": "this would be a key",
        "title_number": title_number,
        "sha256": "a hash of the title below",
        "created_ts": test_creation_time,
        "title": {
            "title_number":  title_number,
            "proprietors": [
            {
                "first_name": "Vile",
                "last_name": "Bawd"
            }
        ],
        "property":{
            "address": {
                "house_number": "1",
                "road": "Muddy Land",
                "town": "The Hovel",
                "postcode": "ABC 123"
            },
            "tenure": "freehold",
            "class_of_title": "absolute"
        },

        "payment": {
            "price_paid": "3",
            "titles": ["AB1234567"]
        }
    }
}

data_for_the_feeder = data_from_mint['title']


class SystemOfRecordTestCase(unittest.TestCase):

    def setUp(self):
        server.app.config["TESTING"] = True
        SQLALCHEMY_DATABASE_URI = "sqlite://"
        server.app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
        db.create_all()
        self.app = server.app.test_client()

    @mock.patch("systemofrecord.feeder.FeederQueue.enqueue")
    @mock.patch("systemofrecord.storage.DBStore.put")
    def test_add_title(self, mock_put, mock_enqueue):
        self.app.put("/titles/%s" % title_number, data = json.dumps(data_from_mint), content_type="application/json")
        mock_put.assert_called_with(title_number, data_from_mint)
        mock_enqueue.assert_called_with(title_number, data_for_the_feeder)

