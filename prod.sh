#!/bin/bash

export PORT=5000
gunicorn -w 1 --bind "0.0.0.0:$PORT" wsgi:app
