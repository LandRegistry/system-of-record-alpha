#!/bin/bash

# TODO potentially mv this to run.sh if run.sh isn't needed anymore.

python manage.py db upgrade
python run_dev.py
