from datatypes.core import DictionaryValidator
from voluptuous import Required, Optional

schema = {
    Required('object_info'): {
        Optional('created_by'): str,
        Required('initial_request_timestamp'): long,
        Optional('reason_for_change'): str,
        Required('schema_version'): int
    },

    Required('object'): {
        Required('object_id'): str,
        Optional('data'): str,

        Optional('tags'): [
            {
                Required('tag_type'): str,
                Required('tag_id'): str,
            }
        ]
    }
}


class SystemOfRecordRequestValidator(DictionaryValidator):
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
