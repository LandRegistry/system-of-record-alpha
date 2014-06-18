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

@app.route('/titles', methods=[ 'GET', 'POST'])
def titles():
    if request.method == 'GET':
        # a bit hokey but for the moment I'll just return urls to
        titles = storage.list_titles()
        print titles
        return jsonify(titles=titles)
    else:
        storage.put(request.json)
        return make_response('OK', 200)
