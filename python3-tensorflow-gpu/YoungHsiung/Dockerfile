FROM tensorflow/tensorflow:latest
MAINTAINER markliou <markliou@ms51.url.com.tw>

RUN apt update -y;\
    apt install python3-pip -y;\
    apt install vim -y;\
    pip3 install tensorflow;\
    pip3 install tqdm;\
    pip3 install Pillow;\
    pip3 install scipy;\
    pip3 install keras;\
    pip3 install dill;\
    pip3 install ktext;\
    pip3 install h5py;\
    pip3 install pandas;\
    pip3 install grpcio;\
    pip3 install Flask;\
    pip3 install futures;\
    pip3 install redis

RUN mkdir /workspace
WORKDIR /workspace
    
# IPython    
EXPOSE 8888
# TensorBoard 
EXPOSE 6006   
    
CMD ["bash"]