#!/bin/bash
gunicorn -c wsgi.config.py wsgi
