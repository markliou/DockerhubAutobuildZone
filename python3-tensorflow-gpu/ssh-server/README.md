Tensorflow with ssh server
==
This repo contain 3 main block

# Dockerfile
This can build a container with:
1. Tensorflow-gpu (so, this is nvidia-docker only)
2. python3
3. ssh server (root/root as account and password)

# deploy script
Build_tensorflow_server.sh will build several ssh servers with continuous ports.
```shell
./Build_tensorflow_server.sh
```
The parameters are discribe as below
1. server_no: set the container you want to build
2. ssh_start_port: the host port can diretly be binded with the container. This parameter set the initial port number. For example, if you set 50000 and build 5 ssh servers, the ports, 50000~50004, will directly connect to the container ssh port(22).

# kill script
kill_tensorflow_server.sh will kill all the containers built with Build_tensorflow_server.sh