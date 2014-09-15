import simplejson
from zlib import compress

from systemofrecord import db
from systemofrecord.models import Title


class InvalidTitleIdException(Exception):
    pass


class DBStore(object):
    def store_title(self, title_number, data):
        # TODO check data integrity using public key
        # (or introduce some chain object to handle validation and
        # then just delegate to some storage mechanism for write of file)

        try:
            if title_number != data['title_number']:
                raise InvalidTitleIdException
        except KeyError:
            raise InvalidTitleIdException

        title = Title(
            title_number=title_number,
            creation_timestamp=1,
            data=(compress(simplejson.dumps(data)))
        )

        db.session.add(title)
        db.session.commit()

    def load_title(self, title_number):
        print "Loading title " + title_number

        for foo in Title.query:
            print "* loaded title: " + repr(foo.as_dict())

        title = Title.query.filter_by(title_number=title_number).first()

        print "***** title is " + repr(title.as_dict())

        if title:
            return title.as_dict()
        else:
            return None

    # def list_titles(self):
    # titles = Title.query
    # if titles:
    #         all_titles = {}  # initialise to append new values
    #         # all_titles dictionary has title_id as index, then title detail as value.
    #
    #         for title in Title.query:
    #             all_titles[title.id] = title.as_dict()
    #
    #         return all_titles
    #     else:
    #         return {}

    def count(self):
        return Title.query.count()

    def health(self):
        try:
            self.count()
            return True, "DB"
        except:
            return False, "DB"
