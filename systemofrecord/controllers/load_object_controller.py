from flask import jsonify, abort

from systemofrecord import app, storage


class LoadObjectController(object):
    def load_object(self, object_id):
        loaded_object = storage.load_object(object_id)

        if loaded_object:
            return jsonify(loaded_object)

        app.logger.info("Could not find title number %s" % object_id)
        return abort(404)