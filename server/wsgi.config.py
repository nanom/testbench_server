# Reference: https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py
# coding=utf-8

# --- Declare imports ---
import os
import multiprocessing
from dotenv import load_dotenv

# --- Own ---
import paths as _path


# --- Load enviroment vars ---
load_dotenv()
SERVER_PORT = os.getenv('SERVER_PORT')
SERVER_HOST = os.getenv('SERVER_HOST')


# --- Declare path to log and socket file save ---
# ETC = os.path.join(_path.ROOT, 'etc')
# VAR = os.path.join(_path.ROOT, 'var')


# --- Declare vars and settings ---

# errorlog = os.path.join(VAR, 'api-error.log')
errorlog = "-"

# accesslog = os.path.join(VAR, 'api-access.log')
accesslog = "-"

# bind = 'unix:%s' % os.path.join(_VAR, 'run/gunicorn.sock')
bind = SERVER_HOST+":"+SERVER_PORT

# --- Para request async se necesita setear gevent en worker_class (no workers) ---
# workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gevent'
max_requests = 10

# 3 minutes
timeout = 3 * 60

# 1 day
keepalive = 24 * 60 * 60
capture_output = True
loglevel = 'info'
