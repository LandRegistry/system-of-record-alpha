from systemofrecord import app
from systemofrecord.services.queue_provider import RedisQueueProvider
ingest_queue = RedisQueueProvider(app.config.get('INGEST_QUEUE_NAME'))

from systemofrecord.services.ingest_queue_producer import IngestQueueProducer

ingest_queue_producer = IngestQueueProducer()




