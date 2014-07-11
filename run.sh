#!/bin/bash

export SYSTEMOFRECORD_URL=foo
export SETTINGS='config.Config'
export DATABASE_URL='postgresql://localhost/sysofrec'
export HTTP_URL=0.0.0.0:5000

foreman start

