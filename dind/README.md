docker-in-docker
===
This image uses  
* ubuntu as OS base
* dind [rc23](!https://github.com/docker-library/docker/blob/7a7c807686f54b67646bc75d2c81a68f9a906dbd/23.0-rc/dind/Dockerfile) for hacked docker-in-docker

## notes
1. docker-in-docker would be good to use the privileged container
2. docker-in-docker cannot execute in iteraction (prompt) mode. The daemon mode is recommended. 

## howt to run
* build the container image:
```
sudo docker build -t markliou/dind .
```
This will build a docker image with name of markliou/dind .
* run the container
```
# the basic mode
sudo docker run -d --rm --privileged markliou/dind 
# GPU available. The host also need to install the nvidia-docker
sudo docker run -d --rm --gpus all --privileged markliou/dind
```
You can also use the -it option for foreground execution. But remember, never use any command after the container. Or this will make the error. 

The final step is to start a new prompt for working.
```
sudo docker exec -it XXXXXX
```
XXXXX means the container number when you initiate a the daemon container. 
You can also run use GPUs with --gpus options with the in-side docker container (but the outside docker-in-docker container **also need to give the --gpus options**)

## references 
* https://github.com/cruizba/ubuntu-dind
* https://jiapan.me/2018/%E4%BD%BF%E7%94%A8-Supervisord-%E5%AE%9E%E7%8E%B0%E8%BF%9B%E7%A8%8B%E7%9B%91%E6%8E%A7/
* https://github.com/docker-library/docker/blob/master/Dockerfile-dind.template
* https://github.com/docker-library/docker/blob/7a7c807686f54b67646bc75d2c81a68f9a906dbd/23.0-rc/dind/Dockerfile

