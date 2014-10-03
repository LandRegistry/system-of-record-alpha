from systemofrecord import configure_logging
from systemofrecord.models import Chain
from systemofrecord import db
from systemofrecord.models.blockchain_object import BlockchainObject


class ChainRepository(object):
    def __init__(self):
        self.logger = configure_logging(self)


    def load_chain_heads_for_object(self, object):
        chains = object.chains
        result = {}
        blockchain_object = None

        if chains:
            for chain in chains:
                query = db.session.query(Chain, BlockchainObject) \
                    .filter(Chain.name == chain.name, Chain.value == chain.value) \
                    .filter(Chain.record_id == BlockchainObject.id) \
                    .filter(BlockchainObject.blockchain_index < object.blockchain_index) \
                    .order_by(BlockchainObject.blockchain_index.desc())

                query_result = query.first()

                if query_result:
                    (found_chain, blockchain_object) = query_result

                if blockchain_object:
                    result[found_chain.name] = blockchain_object

        return result