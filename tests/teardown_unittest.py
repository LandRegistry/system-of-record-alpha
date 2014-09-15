from unittest import TestCase

from systemofrecord import server
from systemofrecord.models import BlockchainObject


class TeardownUnittest(TestCase):
    def setUp(self):
        self.app = server.app.test_client()

    def tearDown(self):
        BlockchainObject.query.delete()