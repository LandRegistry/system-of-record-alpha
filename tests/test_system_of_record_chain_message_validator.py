from unittest import TestCase

from systemofrecord.datatypes import system_of_record_chain_message_validator
from chain_message_fixtures import valid_chain_message, another_valid_message


class ChainMessageValidatorTestCase(TestCase):
    def test_can_validate_message(self):
        system_of_record_chain_message_validator.validate(valid_chain_message)
        system_of_record_chain_message_validator.validate(another_valid_message)