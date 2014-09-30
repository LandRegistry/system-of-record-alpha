from systemofrecord import configure_logging
from systemofrecord.models import Chain


class ChainRepository(object):
    def __init__(self):
        self.logger = configure_logging(self)


    def load_chain_heads_for_object(self, object):
        chains = object['chains']
        result = {}

        if chains:
            for chain in chains:
                # TODO: Currenty ordering by record_id, need to order by blockchain_seq in parent
                chain_name = chain['chain_name']

                result[chain_name] = Chain.query \
                    .filter_by(name=chain_name, value=chain['chain_value']) \
                    .order_by(Chain.record_id.desc()) \
                    .first()

        return result