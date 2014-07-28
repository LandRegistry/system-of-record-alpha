from .server import app
from systemofrecord import db
from systemofrecord.models import Title

class DBStore(object):

    def put(self, title_number, data):
        # TODO check data integrity using public key
        # (or introduce some chain object to handle validation and
        # then just delegate to some storage mechanism for write of file)
        # TODO save data to PostgresQL DB
        title = Title(title_number, str(data)) # change to store json
        db.session.add(title)
        db.session.commit()

    def get(self, title_number):
        title = Title.query.filter_by(title_number=title_number).first()
        if title:
            app.logger.info("Found title %s" % title)
            return {
                'title': {
                    'number':   title.title_number,
                    'data': title.data
            }}
        return None

    def list_titles(self):
        titles = Title.query
        if titles:
            app.logger.info("Found some titles")
            all_titles = {} #initialise to append new values
            #all_titles dictionary has title_id as index, then title detail as value.
            for p in Title.query:
                all_titles[p.id] = {
                     'title': {
                         'number':   p.title_number,
                        'data': p.data
                }}
            return all_titles
        return {}

    def health(self):
        try:
            Title.query.count()
            return True, "DB" 
        except:
            return False, "DB" 
