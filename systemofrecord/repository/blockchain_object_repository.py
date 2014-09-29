from systemofrecord.repository.message_id_validator import check_object_id_matches_id_in_message
from systemofrecord.services.json_conversion import to_json

from systemofrecord.services.compression_service import compress
from systemofrecord import db, configure_logging
from systemofrecord.models import BlockchainObject


class BlockchainObjectRepository(object):
    def __init__(self):
        self.logger = configure_logging(self)

    def store_object(self, object_id, data):
        check_object_id_matches_id_in_message(data, object_id)

        obj_to_store = BlockchainObject(
            object_id=object_id,
            creation_timestamp=1,
            data=compress(to_json(data))  # TODO: We assume all objects are JSON here...
        )

        db.session.add(obj_to_store)
        self.logger.info("Storing object %s" % object_id)
        db.session.commit()

    def load_object(self, object_id):
        object = BlockchainObject.query.filter_by(object_id=object_id).first()

        if object:
            return object
            #return object.as_dict()

        return None


    def count(self):
        return BlockchainObject.query.count()

    def health(self):
        try:
            self.count()
            return True, "DB"
        except:
            return False, "DB"
