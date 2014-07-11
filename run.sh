#!/bin/bash

export SETTINGS='config.Config'
export DATABASE_URL='postgresql://localhost/sysofrec'

createuser -s sysofrec
createdb -U sysofrec -O sysofrec sysofrec -T template0

python manage.py db upgrade

foreman start

