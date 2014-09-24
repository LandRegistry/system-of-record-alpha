# -*- coding: utf-8 -*-


# strip out any of the generated fields that get put on an object when it is loaded
# to simplify comparisons. We'll check that the fields are present before we delete
# them, as their absence suggests that a load operation did not work correctly.
def remove_generated_fields_from_loaded_object(obj):
    info = obj['object_info']
    assert info
    assert info['db_id']
    assert info['creation_timestamp']
    assert info['blockchain_index']

    del info['db_id']
    del info['creation_timestamp']
    del info['blockchain_index']
    return obj


valid_system_of_record_input_message = {

    'object_info': {
        'created_by': 'The Mint',
        'initial_request_timestamp': '123456',
        'reason_for_change': "str",
        'schema_version': 1
    },


    'object': {
        'object_id': 'AB12345',
        'data': '<data>',

        'tags': [
            {
                'tag_type': 'version',
                'tag_id': 'foo',
                'tag_uri': "http://sysofrec/tags/foo",
                }
        ],
    }
}

valid_message_without_tags = {
    'object_info': {
        'created_by': 'The Mint',
        'initial_request_timestamp': '123456',
        'reason_for_change': "str",
        'schema_version': 1
    },

    'object': {
        'object_id': 'AB12345',
        'data': '<data>'
    }
}

invalid_message_without_schema_version = {
    'object_info': {
        'created_by': 'The Mint',
        'initial_request_timestamp': '123456',
        'reason_for_change': "str",
    },


    'object': {
        'object_id': 'AB12345',
        'data': '<data>',

        'tags': [
            {
                'tag_type': 'version',
                'tag_id': 'foo',
                'tag_uri': "http://sysofrec/tags/foo",
                }
        ],
    }
}

invalid_message_with_extra_keys = {
    'object_info': {
        'created_by': 'The Mint',
        'initial_request_timestamp': '123456',
        'reason_for_change': "str",
        },

    'extra-key': 'foo',

    'object': {
        'object_id': 'AB12345',
        'data': '<data>',

        'tags': [
            {
                'tag_type': 'version',
                'tag_id': 'foo',
                'tag_uri': "http://sysofrec/tags/foo",
                }
        ],
    }
}

invalid_message_without_object = {
    'object_info': {
        'created_by': 'The Mint',
        'initial_request_timestamp': '123456',
        'reason_for_change': "str",
        'schema_version': 1
    },
}
