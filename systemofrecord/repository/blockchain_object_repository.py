import simplejson

from systemofrecord.services.compression_service import compress
from systemofrecord import db
from systemofrecord.models import BlockchainObject


class InvalidTitleIdException(Exception):
    pass


class BlockchainObjectRepository(object):
    def store_object(self, object_id, data):
        # TODO check data integrity using public key
        # (or introduce some chain object to handle validation and
        # then just delegate to some storage mechanism for write of file)

        try:
            if object_id != data['object']['object_id']:  # TODO: Change to object_id
                raise InvalidTitleIdException
        except KeyError:
            raise InvalidTitleIdException

        title = BlockchainObject(
            object_id=object_id,
            creation_timestamp=1,
            data=compress(simplejson.dumps(data))
        )

        db.session.add(title)
        db.session.commit()

    def load_object(self, title_number):
        title = BlockchainObject.query.filter_by(object_id=title_number).first()

        if title:
            return title.as_dict()

        return None


    def count(self):
        return BlockchainObject.query.count()

    def health(self):
        try:
            self.count()
            return True, "DB"
        except:
            return False, "DB"
