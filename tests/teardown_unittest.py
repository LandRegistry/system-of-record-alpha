from unittest import TestCase

from systemofrecord import server
from systemofrecord.services import ingest_queue, feeder_queue
from systemofrecord.models import BlockchainObject


class TeardownUnittest(TestCase):
    def consume_queues(self):
        while not ingest_queue.is_empty():
            ingest_queue.read_from_queue()

        while not feeder_queue.is_empty():
            feeder_queue.read_from_queue()

    def setUp(self):
        super(TeardownUnittest, self).setUp()
        self.app = server.app.test_client()
        self.consume_queues()


    def tearDown(self):
        super(TeardownUnittest, self).tearDown()
        BlockchainObject.query.delete()
        self.consume_queues()