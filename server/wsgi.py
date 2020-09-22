from server import app as application
import os

if __name__ == '__main__':
    application.run()

# gunicorn server:app -k gevent -b 192.168.0.36:9090
# RUN using gunicorn -c wsgi.config wsgi.py
