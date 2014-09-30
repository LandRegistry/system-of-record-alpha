from systemofrecord import configure_logging
from systemofrecord.services import chain_queue
from systemofrecord.datatypes import system_of_record_chain_message_validator


class ChainQueueProducer(object):
    def __init__(self):
        self.logger = configure_logging(self)

    def enqueue_for_object(self, originating_object, chains):
        message_to_send = self.create_chain_message(originating_object, chains)
        system_of_record_chain_message_validator.validate(message_to_send)
        chain_queue.add_to_queue(message_to_send)
        self.logger.debug("Chain message sent: " + repr(message_to_send))

    def create_chain_message(self, originating_object, chains):
        return {
            'message_envelope': {
                'caused_by_blockchain_insert_id': int(originating_object.as_dict()['object']['blockchain_index']),
                'messages': self.chain_message_content(chains)
            }
        }

    def chain_message_content(self, chains):
        message_content = []
        for chain_name in chains.iterkeys():
            chain_message = chains[chain_name].as_dict()
            del chain_message['chains']

            message_content.append({
                'chain_name': str(chain_name),
                'message': chain_message,
            })

        return message_content