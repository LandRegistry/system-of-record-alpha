from systemofrecord.datatypes import system_of_record_request_validator


class SystemOfRecordIngestor(object):
    def ingest(self, message):
        system_of_record_request_validator.validate(message)
        assert False == True

