# haskell_testbench_server

**How to use localy.**
- *For run server execute:*
    ```$ ./server/run.sh```
- *For install server requirements:*
    ```$ pip install -r requirements.txt```
-  ***'server/wsgi.config.py'** for configure server parameters (port, hostname, max_request, etc).*

**Use througth docker. (Note: In this particular case, the port and host should be setting to 0.0.0.0 and 5000 respectively)**
- *1) Building a docker image:*
    ```$ sudo docker build -t 'name_of_image' -f Dockerfile```
- *2) Executing server:*
    - *Through docker image:*
    ```$ sudo docker run --rm -it -p host:host_port:5000 'name_of_image'```
    - *Create and execute container from the image:*
        1) *Creating container:*
        ```$ sudo docker create --name 'container_name' -p host:host_port:5000 'name_of_image' ```
        2) *Executing container:*
        ```$ sudo docker start 'container_name' ```
