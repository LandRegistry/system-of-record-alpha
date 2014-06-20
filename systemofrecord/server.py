from flask import jsonify,  abort, request, make_response
from simplejson import load

from systemofrecord import app
from .storage import S3Store, MemoryStore

if not (app.config['AWS_KEY'] and app.config['AWS_SECRET'] and app.config['S3_BUCKET']):
    storage = MemoryStore()
else:
    storage = S3Store(app.config)
    app.logger.info( 'Running against S3')

@app.route('/titles/<title_number>')
def  title_by_number(title_number):
        title = storage.get(title_number)
        if not title:
            app.logger.info( 'Title number: %s not found ' % title_number)
            abort(404)
        #jiggery pokery for stupid in memory storage thing i did
        if type(title) != dict:
            title = load(title)
        return jsonify({title_number : title})

@app.route('/titles', methods=[ 'GET', 'POST'])
def titles():
    if request.method == 'GET':
        titles = storage.list_titles()
        return jsonify(titles=titles)
    else:
        storage.put(request.json)
        return make_response('OK', 200)
