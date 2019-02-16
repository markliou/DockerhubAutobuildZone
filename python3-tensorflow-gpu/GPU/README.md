
## [How to specifiy the enviroment in container](https://stackoverflow.com/questions/30494050/how-do-i-pass-environment-variables-to-docker-containers)

* Use '-e' tag for this purpose.  
For example:  
```
docker run -it --rm -e CUDA_VISIBLE_DEVICES=1 <container>
```
