#!/bin/bash

export SYSTEMOFRECORD_URL=foo
export SETTINGS='config.Config'
export DATABASE_URL='postgresql://localhost/sysofrec'

foreman start
export HTTP_URL=0.0.0.0:5000

