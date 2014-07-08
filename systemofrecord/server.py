from flask import jsonify,  abort, request, make_response
from simplejson import load

from systemofrecord import app
from .storage import DBStore, MemoryStore

if app.config['USE_INMEMORY_DB']:
    print "Using in-memory storage"
    storage = MemoryStore()
else:
    print "Using DB storage"
    storage = DBStore(app)


@app.route('/titles/last', methods=['GET', 'POST'])
def last_title():
    if request.method == 'GET':
        last_title = storage.get_last()
        if last_title:
            return jsonify(last_title)
        else:
            return abort(404)
    else:
        storage.put_last(request.json)
        return make_response('OK', 200)

@app.route('/titles/<number>', methods=['GET', 'POST'])
def by_title(number=None):
    if request.method == 'GET':
        title = storage.get(number)
        if title:
            return jsonify(title)
        else:
            return abort(404)
    else:
        storage.put(number, request.json)
        #app.logger.debug("number %s, data %s" %(number, request.json))
        return make_response('OK', 200)



#not sure who this would be for yet.
@app.route('/titles')
def titles():
    titles = storage.list_titles()
    return jsonify(titles=titles)
