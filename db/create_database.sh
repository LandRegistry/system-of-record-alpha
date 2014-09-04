#!/bin/bash

echo "Creating database for system-of-record"

createuser -s sysofrec
createdb -U sysofrec -O sysofrec sysofrec -T template0
