from flask import request

from systemofrecord import app
from systemofrecord.controllers import load_title_controller, store_title_controller


@app.route('/titles/<title_number>', methods=['GET', 'PUT'])
def title(title_number):
    app.logger.debug("Title number %s, data %s" % (title_number, request.json))

    if request.method == 'GET':
        return load_title_controller.load_title(title_number)
    else:
        return store_title_controller.store_title(title_number, request.json)