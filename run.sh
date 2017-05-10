#!/usr/bin/env bash

cd /code
uwsgi --http 0.0.0.0:5000 --wsgi-file test.py --callable app --processes 4 --threads 2