from datatypes.exceptions import DataDoesNotMatchSchemaException
from unittest import TestCase

from systemofrecord.datatypes import system_of_record_request_validator
from system_of_record_message_fixtures import *


class SystemOfRecordRequestValidatorTestCase(TestCase):
    def test_can_validate_system_of_record_request(self):
        try:
            system_of_record_request_validator.validate(valid_system_of_record_input_message_with_two_tags)
            system_of_record_request_validator.validate(valid_message_without_tags)
        except DataDoesNotMatchSchemaException as e:
            self.fail("Should not have thrown " + repr(e))


    def test_does_not_accept_invalid_message(self):
        self.assertRaises(DataDoesNotMatchSchemaException, system_of_record_request_validator.validate, invalid_message_without_object)
        self.assertRaises(DataDoesNotMatchSchemaException, system_of_record_request_validator.validate, invalid_message_without_schema_version)
        self.assertRaises(DataDoesNotMatchSchemaException, system_of_record_request_validator.validate, invalid_message_with_extra_keys)