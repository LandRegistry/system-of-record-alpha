from unittest import TestCase

from systemofrecord import server
from systemofrecord.models import BlockchainObject


class TeardownUnittest(TestCase):
    def setUp(self):
        super(TeardownUnittest, self).setUp()
        self.app = server.app.test_client()

    def tearDown(self):
        super(TeardownUnittest, self).tearDown()
        BlockchainObject.query.delete()