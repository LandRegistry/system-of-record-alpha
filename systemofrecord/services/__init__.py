from systemofrecord.services.queue_provider import QueueProvider
from systemofrecord import app


queue_provider = QueueProvider(app.config.get('INGEST_QUEUE_NAME'))


