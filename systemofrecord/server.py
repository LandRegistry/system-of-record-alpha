from flask import jsonify,  abort, request, make_response

from systemofrecord import app
from .storage import DBStore
from .feeder import FeederQueue

feeder = FeederQueue(app)
storage = DBStore()

@app.route('/')
def index():
  return "OK"

@app.route('/title/<title_number>', methods=['GET', 'POST'])
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
        return make_response('OK', 200)

@app.route('/title')
def titles():
    titles = storage.list_titles()
    return jsonify(titles=titles)


