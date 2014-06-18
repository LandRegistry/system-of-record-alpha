from flask import jsonify,  abort, request, make_response
from simplejson import load

from systemofrecord import app
from .storage import Storage

storage = Storage(app.config)

@app.route('/titles/<title_number>')
def  title_by_number(title_number):
        print "calling titles with number %s" % title_number
        title = storage.get(title_number)
        if title:
            return jsonify(load(title))
        abort(404)

@app.route('/titles', methods=[ 'POST'])
def titles():
    storage.put(request.json)
    return make_response('OK', 200)
