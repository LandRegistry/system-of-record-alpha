from systemofrecord.services.json_conversion import parse_json_from_request

from systemofrecord import app
from systemofrecord.controllers import load_title_controller, store_title_controller


@app.route('/titles/<object_id>', methods=['GET'])
def get_object(object_id):
    return load_title_controller.load_object(object_id)


@app.route('/titles/<object_id>', methods=['PUT'])
def store_object(object_id):
    app.logger.info("Requested to store object_id: %s" % object_id)
    return store_title_controller.store_object(object_id, parse_json_from_request())
