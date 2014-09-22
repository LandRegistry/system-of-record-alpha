from flask import jsonify, abort

from systemofrecord import app

from systemofrecord.repository import blockchain_repository


class LoadObjectController(object):
    def load_object(self, object_id):
        loaded_object = blockchain_repository.load_object(object_id)

        if loaded_object:
            return jsonify(loaded_object)

        app.logger.info("Could not find object with ID: %s" % object_id)
        return abort(404)