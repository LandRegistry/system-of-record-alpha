from flask import jsonify,  abort, request, make_response

from systemofrecord import app
from .storage import DBStore

storage = DBStore(app)

@app.route('/', methods=['GET'])
def index():
  return "OK"

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
        queue_title(number, request.json)
        #app.logger.debug("number %s, data %s" %(number, request.json))
        return make_response('OK', 200)

@app.route('/titles')
def titles():
    titles = storage.list_titles()
    return jsonify(titles=titles)

# TODO refactor and move to own module
from redis import Redis
redis_host = app.config.get('REDIS_HOST')
redis_queue = app.config.get('REDIS_QUEUE')
redis = Redis(redis_host)

def queue_title(number, json):
    try:
        redis.rpush(redis_queue, json)
    except Exception, e:
        app.logger.info(e)
        app.logger.info("Couldn't enqueue data for title %s: data: %s" % (number, json))
