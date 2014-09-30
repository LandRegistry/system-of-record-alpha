valid_chain_message = {
    'message_envelope': {
        'caused_by_blockchain_insert_id': 3954,

        'messages': [
            {
                'message': {
                    'object': {
                        'reason_for_change': 'str',
                        'db_id': 3953,
                        'data': '<data>',
                        'initial_request_timestamp': '123456',
                        'created_by': 'The Mint',
                        'creation_timestamp': 1,
                        'object_id': 'AB12345',
                        'chains': [
                            {'chain_name': 'history', 'chain_value': 'AB12345'},
                            {'chain_name': 'sausage', 'chain_value': 'walls'}
                        ],
                        'blockchain_index': 3953
                    },
                },
                'chain_name': 'sausage',
            },
            {
                'message': {
                    'object': {
                        'reason_for_change': 'str',
                        'db_id': 3953,
                        'data': '<data>',
                        'initial_request_timestamp': '123456',
                        'created_by': 'The Mint',
                        'creation_timestamp': 1,
                        'object_id': 'AB12345',
                        'chains': [
                            {'chain_name': 'history', 'chain_value': 'AB12345'},
                            {'chain_name': 'sausage', 'chain_value': 'walls'}
                        ],
                        'blockchain_index': 3953
                    },
                },
                'chain_name': 'history',
            }
        ]
    }
}

another_valid_message = {
    'message_envelope': {
        'caused_by_blockchain_insert_id': 4188,
        'messages': [
            {'message': {
                'object': {'reason_for_change': 'str', 'db_id': 4187, 'data': '<data>',
                           'initial_request_timestamp': '123456',
                           'created_by': 'The Mint', 'creation_timestamp': 1, 'object_id': 'AB12345',
                           'chains': [{'chain_name': 'history', 'chain_value': 'AB12345'},
                                      {'chain_name': 'sausage', 'chain_value': 'walls'}], 'blockchain_index': 4187}},
             'chain_name': 'sausage'
            },
            {
                'message': {
                    'object': {'reason_for_change': 'str',
                               'db_id': 4187,
                               'data': '<data>',
                               'initial_request_timestamp': '123456',
                               'created_by': 'The Mint',
                               'creation_timestamp': 1,
                               'object_id': 'AB12345',
                               'chains': [{
                                              'chain_name': 'history',
                                              'chain_value': 'AB12345'},
                                          {
                                              'chain_name': 'sausage',
                                              'chain_value': 'walls'}],
                               'blockchain_index': 4187}},
                'chain_name': 'history'
            }
        ]
    }
}

