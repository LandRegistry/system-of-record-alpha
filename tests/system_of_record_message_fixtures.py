valid_system_of_record_input_message = {

    'object_info': {
        'created_by': 'The Mint',
        'initial_request_timestamp': long(123456),
        'reason_for_change': "str",
        'schema_version': 1
    },

    'tags': [
        {
            'tag_type': 'version',
            'tag_id': 'foo',
            'tag_uri': "http://sysofrec/tags/foo",
        }
    ],

    'object': {
        'object_id': 'AB12345',
        'data': '<data>'
    }
}

valid_message_without_tags = {
    'object_info': {
        'created_by': 'The Mint',
        'initial_request_timestamp': long(123456),
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
        'initial_request_timestamp': long(123456),
        'reason_for_change': "str",
    },

    'tags': [
        {
            'tag_type': 'version',
            'tag_id': 'foo',
            'tag_uri': "http://sysofrec/tags/foo",
        }
    ],

    'object': {
        'object_id': 'AB12345',
        'data': '<data>'
    }
}

invalid_message_without_object = {
    'object_info': {
        'created_by': 'The Mint',
        'initial_request_timestamp': long(123456),
        'reason_for_change': "str",
        'schema_version': 1
    },

    'tags': [
        {
            'tag_type': 'version',
            'tag_id': 'foo',
            'tag_uri': "http://sysofrec/tags/foo",
        }
    ],
}
