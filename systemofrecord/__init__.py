import os, sys
from flask import Flask
from flask.ext.basicauth import BasicAuth

app = Flask(__name__)


app.config.from_object('config')
if not (app.config['AWS_KEY'] and app.config['AWS_SECRET']  and app.config['S3_BUCKET']):
    print "Please set the following environment variables: AWS_KEY, AWS_SECRET and S3_BUCKET"
    print "Currently they are set to AWS_KEY=%s : AWS_SECRET=%s : S3_BUCKET=%s" %  (app.config['AWS_KEY'], app.config['AWS_SECRET'], app.config['S3_BUCKET'])
    sys.exit(-1)

# auth
if os.environ.get('BASIC_AUTH_USERNAME'):
    app.config['BASIC_AUTH_USERNAME'] = os.environ['BASIC_AUTH_USERNAME']
    app.config['BASIC_AUTH_PASSWORD'] = os.environ['BASIC_AUTH_PASSWORD']
    app.config['BASIC_AUTH_FORCE'] = True
    basic_auth = BasicAuth(app)


