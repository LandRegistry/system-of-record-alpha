from flask import make_response

from systemofrecord import storage, app, feeder_queue


class StoreTitleController(object):
    def store_title(self, title_number, title_as_json):
        storage.store_object(title_number, title_as_json)
        app.logger.info("Put title json %s on feeder queue" % title_as_json['title'])
        feeder_queue.enqueue(title_number, title_as_json['title'])
        app.logger.debug("Title number %s, data %s" % (title_number, title_as_json))
        return make_response('OK', 201)