from datatypes.core import DictionaryValidator
from datatypes.exceptions import DataDoesNotMatchSchemaException
from voluptuous import Required, Optional, Coerce


schema = {

    Required('object'): {
        Required('object_id'): str,
        Required('data'): str,
        Optional('created_by'): str,
        Optional('initial_request_timestamp'): Coerce(long),
        Optional('reason_for_change'): str,

        Optional('chains'): [
            {
                Required('chain_name'): str,
                Required('chain_value'): str,
            }
        ]
    }
}


class SystemOfRecordRequestValidator(DictionaryValidator):
    def validate(self, dictionary):
        super(SystemOfRecordRequestValidator, self).validate(dictionary)

        try:
            chains = dictionary['object']['chains']
            chain_names = {}

            for chain in chains:
                chain_name = chain['chain_name']
                if not chain_names.get(chain_name):
                    chain_names[chain_name] = 1
                else:
                    raise DataDoesNotMatchSchemaException(message="Message contained duplicate chain name %s" % chain_name)
        except KeyError:
            pass

    def define_schema(self):
        return schema

    def define_error_dictionary(self):
        return {
            'object_info': 'object_info is required',
            'object_info.created_by': 'created_by must be a string',
            'object_info.initial_request_timestamp': 'initial_request_timestamp is mandatory and must be a long',
            'object_info.reason_for_change': 'reason_for_change must be a string',
            'object_info.schema_version': 'schema_version is required and must be an integer',
            'tags': 'tags must be a list of tag objects [{tag_type, tag_id}]',
            'object': 'An object to store is required {object_id, data}',
            'object.object_id': 'object_id is required and must be a string',
            'object.data': 'data is required and must be a string'
        }

