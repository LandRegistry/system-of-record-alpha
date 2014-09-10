from flask import jsonify,  abort, request, make_response

from systemofrecord import app

from repository import DBStore
from .feeder import FeederQueue
from .health import Health

storage = DBStore()
feeder = FeederQueue(app)
Health(app, checks=[storage.health, feeder.health])


@app.route('/titles/<title_number>', methods=['GET', 'PUT'])
def title(title_number):
    app.logger.debug("Title number %s, data %s" %(title_number, request.json))

    if request.method == 'GET':
        title = storage.load_title(title_number)
        if title:
            return jsonify(title)
        else:
            app.logger.info("Could not find title number %s" % title_number)
            return abort(404)
    else:
        storage.store_title(title_number, request.json)
        app.logger.info("Put title json %s on feeder queue" % request.json['title'])
        feeder.enqueue(title_number, request.json['title'])
        app.logger.debug("Title number %s, data %s" %(title_number, request.json))
        return make_response('OK', 201)

# @app.route('/titles')
# def titles():
#     titles = storage.list_titles()
#     return jsonify(titles=titles)
