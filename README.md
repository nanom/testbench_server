# haskell_testbench_server

**How to use localy:**
- *For run server execute:*
    ```$ ./server/run.sh```
- *For install server requirements:*
    ```$ pip install -r requirements.txt```
-  ***'server/wsgi.config.py'** for configure server parameters (port, hostname, max_request, etc).*

**Use througth docker:**
- *1) Building a docker image:*
- ```$ sudo docker build -t 'name_of_image' -f Dockerfile```
- *1) Executing docker image:*
- ```$ sudo docker run --rm -it -p host:port:5000 'name_of_image'```
