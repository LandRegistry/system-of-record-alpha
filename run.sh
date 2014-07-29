#!/bin/bash

source ./environment.sh
createuser -s sysofrec
createdb -U sysofrec -O sysofrec sysofrec -T template0

python manage.py db upgrade
python run_dev.py
