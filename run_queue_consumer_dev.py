from systemofrecord import app
from commitbuffer import IngestQueueConsumer
from systemofrecord.services import ingest_queue


if __name__ == '__main__':
    IngestQueueConsumer(
        queue_key=app.config.get("INGEST_QUEUE_NAME"),
        queue=ingest_queue,
    ).run()
