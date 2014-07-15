#!/bin/bash

export SETTINGS='config.DevelopmentConfig'
export DATABASE_URL='postgresql://localhost/sysofrec'
export REDIS_QUEUE_KEY='titles_queue'
export REDIS_HOST='redis://user:@localhost:6379'

createuser -s sysofrec
createdb -U sysofrec -O sysofrec sysofrec -T template0

python manage.py db upgrade
python run_dev.py
