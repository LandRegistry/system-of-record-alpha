from flask import jsonify, abort

from systemofrecord import app, storage


class LoadTitleController(object):
    def load_title(self, title_number):
        loaded_title = storage.load_title(title_number)

        if loaded_title:
            return jsonify(loaded_title)

        app.logger.info("Could not find title number %s" % title_number)
        return abort(404)