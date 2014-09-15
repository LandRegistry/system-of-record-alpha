from flask import request

from systemofrecord import app
from systemofrecord.controllers import load_title_controller, store_title_controller


@app.route('/titles/<title_number>', methods=['GET'])
def get_title(title_number):
    return load_title_controller.load_object(title_number)


@app.route('/titles/<title_number>', methods=['PUT'])
def store_title(title_number):
    app.logger.info("Storing object [title_number: %s], [data: %s]" % (title_number, request.json))
    return store_title_controller.store_title(title_number, request.json)
