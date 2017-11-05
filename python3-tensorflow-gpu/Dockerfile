FROM gcr.io/tensorflow/tensorflow:latest-gpu
MAINTAINER markliou <markliou@ms51.url.com.tw>

RUN apt update -y;\
    apt install python3-pip -y;\
    pip3 install --upgrade pip;\
    pip3 install tensorflow-gpu

RUN mkdir /workspace
WORKDIR /workspace
    
# IPython    
EXPOSE 8888
# TensorBoard 
EXPOSE 6006   
    
CMD ["bash"]