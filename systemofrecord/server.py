from flask import jsonify,  abort, request, make_response

from systemofrecord import app
from .storage import DBStore
from .feeder import FeederQueue

feeder = FeederQueue(app)
storage = DBStore()

@app.route('/', methods=['GET'])
def index():
  return "OK"

# @app.route('/titles/last')
# def last_title():
#     last_title = storage.get_last()
#     if last_title:
#         return jsonify(last_title)
#     else:
#         return abort(404)

@app.route('/titles/<number>', methods=['GET', 'POST'])
def title(number):
    if request.method == 'GET':
        title = storage.get(number)
        if title:
            return jsonify(title)
        else:
            return abort(404)
    else:
        storage.put(number, request.json)
        feeder.enqueue(number, request.json)
        app.logger.debug("number %s, data %s" %(number, request.json))
        return make_response('OK', 200)

@app.route('/titles')
def titles():
    titles = storage.list_titles()
    return jsonify(titles=titles)


