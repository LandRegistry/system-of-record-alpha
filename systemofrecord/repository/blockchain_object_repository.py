from systemofrecord import db, configure_logging
from systemofrecord.models import BlockchainObject


class BlockchainObjectRepository(object):
    def __init__(self):
        self.logger = configure_logging(self)

    def store_object(self, object_id, data):
        self.logger.info("Storing object %s" % object_id)
        db.session.add(BlockchainObject.create(object_id, data))
        db.session.commit()

    def load_object(self, object_id):
        return BlockchainObject.query\
            .filter_by(object_id=object_id)\
            .order_by(BlockchainObject.blockchain_index.desc())\
            .first()

    def count(self):
        return BlockchainObject.query.count()

    def health(self):
        try:
            self.count()
            return True, "DB"
        except:
            return False, "DB"
