# Here we'll create a test database, and override the database to the test values.
set +x
set +o errexit
createuser -s sysofrec_test
createdb -U sysofrec_test -O sysofrec_test sysofrec_test -T template0
set -e
export DATABASE_URL='postgresql://localhost/sysofrec_test'
export INGEST_QUEUE_NAME='test-system-of-record-ingest'
export INGEST_QUEUE_POLL_INTERVAL_IN_SECONDS=1
export FEEDER_QUEUE_NAME='test-titles-queue'
export CHAIN_QUEUE_NAME='test-chain-queue'
