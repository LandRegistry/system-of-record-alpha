from commitbuffer import system_of_record_ingestor


class InputFeedConsumer(object):
    def __init__(self, queue, queue_key, workers):
        self.workers = workers
        self.queue_key = queue_key
        self.queue = queue
        self.current_message = None

    def next_message(self):
        self.current_message = self.queue.blpop(self.queue_key)

    def run(self):
        while True:
            try:
                self.next_message()
                system_of_record_ingestor.ingest(self.current_message)
                # TODO: rate control / sleep?
            except Exception as e:
                # TODO: Clean up logger
                print "Exception processing message [%s], %s" % (repr(self.current_message), repr(e))

