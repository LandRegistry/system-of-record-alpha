from ..server import app
from systemofrecord import db
from systemofrecord.models import Title
import json


class DBStore(object):

    def put(self, title_number, data):
        # TODO check data integrity using public key
        # (or introduce some chain object to handle validation and
        # then just delegate to some storage mechanism for write of file)
        title = Title(title_number, json.dumps(data))
        db.session.add(title)
        db.session.commit()

    def get(self, title_number):
        title = Title.query.filter_by(title_number=title_number).first()
        if title:
            app.logger.info("Found title %s" % title)
            return title.as_dict()
        return None

    def list_titles(self):
        titles = Title.query
        if titles:
            app.logger.info("Found some titles")
            all_titles = {} #initialise to append new values
            #all_titles dictionary has title_id as index, then title detail as value.
            for title in Title.query:
                all_titles[title.id] = title.as_dict()
            return all_titles
        return {}

    def count(self):
        return Title.query.count()


    def health(self):
        try:
            self.count()
            return True, "DB"
        except:
            return False, "DB"
