from flask import jsonify,  abort, request, make_response
from simplejson import load

from systemofrecord import app
from .storage import S3Store, MemoryStore
storage = MemoryStore()

@app.route('/titles/last', methods=[ 'GET', 'POST'])
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


# These need to go to something like a title service that exists at
# the other end of a feeder application

# @app.route('/titles/<title_number>')
# def  latest_title_by_number(title_number):
#         title = storage.get_latest(title_number)
#         if not title:
#             app.logger.info( 'Title number: %s not found ' % title_number)
#             abort(404)
#         #jiggery pokery for stupid in memory storage thing i did
#         if type(title) != dict:
#             title = load(title)
#         return jsonify({title_number : title})

# @app.route('/titles/<title_number>/<int:timestamp>')
# def  title_by_number(title_number, timestamp):
#         title = storage.get_title(title_number, timestamp)
#         if not title:
#             app.logger.info( 'Title number: %s not found ' % title_number)
#             abort(404)
#         #jiggery pokery for stupid in memory storage thing i did
#         if type(title) != dict:
#             title = load(title)
#         return jsonify({title_number : title})


#not sure who this would be for yet.
@app.route('/titles')
def titles():
    titles = storage.list_titles()
    return jsonify(titles=titles)
