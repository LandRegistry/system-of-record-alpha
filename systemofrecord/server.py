from flask import jsonify,  abort, request, make_response

from systemofrecord import app

from .storage import DBStore
from .feeder import FeederQueue
from .health import Health

storage = DBStore()
feeder = FeederQueue(app)
Health(app, checks=[storage.health, feeder.health])

@app.route('/')
def index():
  return "OK"

@app.route('/titles/<title_number>', methods=['GET', 'PUT'])
def title(title_number):

    app.logger.debug("Title number %s, data %s" %(title_number, request.json))

    if request.method == 'GET':
        title = storage.get(title_number)
        if title:
            return jsonify(title)
        else:
            return abort(404)
    else:
        storage.put(title_number, request.json)
        app.logger.info("Put title json %s on feeder queue" % request.json['title'])
        feeder.enqueue(title_number, request.json['title'])
        app.logger.debug("Title number %s, data %s" %(title_number, request.json))
        return make_response('OK', 201)

@app.route('/titles')
def titles():
    titles = storage.list_titles()
    return jsonify(titles=titles)
