from .server import app
from systemofrecord import db
from systemofrecord.models import Titles

class DBStore(object):

    def put(self, title_number, data):
        # TODO check data integrity using public key
        # (or introduce some chain object to handle validation and
        # then just delegate to some storage mechanism for write of file)
        # TODO save data to PostgresQL DB
        title = Titles(title_number, str(data))
        db.session.add(title)
        db.session.commit()

    def get_last(self):
        titles = Titles.query.first()
        if titles:
            return {'title': {
                'number':titles.title_number,
                'data':titles.data
            }}
        return []

    def get(self, title_number):
        title = Titles.query.filter_by(title_number=title_number).first()
        if title:
            app.logger.info("Found title %s" % title)
            return {
                'title': {
                    'number':   title.title_number,
                    'data': title.data
            }}
        return None

    def list_titles(self):
        titles = Titles.query
        if titles:
            app.logger.info("Found some titles")
            all_titles = {} #initialise to append new values
            #all_titles dictionary has title_id as index, then title detail as value.
            for p in Titles.query:
                all_titles[p.id] = {
                     'title': {
                         'number':   p.title_number,
                        'data': p.data
                }}
            return all_titles
        return {}

    def health(self):
        try:
            Titles.query.count()
            return True, "DB" 
        except:
            return False, "DB" 
