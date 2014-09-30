from datatypes.core import DictionaryValidator
from voluptuous import Required

from systemofrecord.datatypes import system_of_record_request_validator


schema = {
    Required('message-envelope'): {
        Required('caused-by-blockchain-insert-id'): int,
        Required('messages'): {
            Required('chain-name'): str,
            Required('messages'): [system_of_record_request_validator.schema]
        }
    }
}


class SystemOfRecordTagMessageValidator(DictionaryValidator):
    def define_schema(self):
        return schema

    def define_error_dictionary(self):
        return {

        }