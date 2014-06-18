from flask import json, request, make_response
from datetime import datetime

from systemofrecord import app
from .storage import Storage

storage = Storage(app.config)

@app.route('/entries', methods=['GET', 'POST'])
def entries():
    if request.method == 'GET':
          return json.dumps({'nothing' : 'here'})
    else:
        storage.put(request.json)
        return "200"
