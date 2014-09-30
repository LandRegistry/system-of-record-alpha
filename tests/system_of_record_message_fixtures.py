# -*- coding: utf-8 -*-

valid_system_of_record_input_message_with_two_tags = {
    'schema_version': 1,

    'object': {
        'object_id': 'AB12345',
        'data': '<data>',
        'created_by': 'The Mint',
        'initial_request_timestamp': '123456',
        'reason_for_change': "str",

        'chains': [
            {
                'chain_name': 'history',
                'chain_value': 'AB12345',
            },
            {
                'chain_name': 'sausage',
                'chain_value': 'walls',
            }
        ],
    }
}

valid_message_without_tags = {
    'schema_version': 1,

    'object': {
        'object_id': 'AB12345',
        'data': '<data>',
        'created_by': 'The Mint',
        'initial_request_timestamp': '123456',
        'reason_for_change': "str",
    }
}

invalid_message_without_schema_version = {

    'object': {
        'object_id': 'AB12345',
        'data': '<data>',
        'created_by': 'The Mint',
        'initial_request_timestamp': '123456',
        'reason_for_change': "str",

        'chains': [
            {
                'chain_name': 'version',
                'chain_value': 'foo',
            }
        ],
    }
}

invalid_message_with_duplicate_tag_value = {
    'object': {
        'object_id': 'AB12345',
        'data': '<data>',
        'created_by': 'The Mint',
        'initial_request_timestamp': '123456',
        'reason_for_change': "str",

        'chains': [
            {
                'chain_name': 'version',
                'chain_value': 'foo',
            },
            {
                'chain_name': 'version',
                'chain_value': 'foo',
            }
        ],
    }
}

another_invalid_message_with_duplicate_tag_value = {
    'object': {
        'object_id': 'AB12345',
        'data': '<data>',
        'created_by': 'The Mint',
        'initial_request_timestamp': '123456',
        'reason_for_change': "str",

        'chains': [
            {
                'chain_name': 'version',
                'chain_value': 'foo',
            },
            {
                'chain_name': 'version',
                'chain_value': 'bar',
            }
        ],
    }
}

invalid_message_with_extra_keys = {
    'object_info': {
        'foo': '1',
    },

    'schema-version': '1',

    'object': {
        'object_id': 'AB12345',
        'data': '<data>',
        'created_by': 'The Mint',
        'initial_request_timestamp': '123456',
        'reason_for_change': "str",

        'chains': [
            {
                'chain_name': 'version',
                'chain_value': 'foo',
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
