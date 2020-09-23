FROM ubuntu:16.04

WORKDIR /www

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev && \
    apt-get install -y haskell-platform

COPY ./requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /www/server

# ENTRYPOINT ["python3", "./server.py"]
# CMD ["run.sh"]
ENTRYPOINT ["/bin/bash", "./run.sh"]
