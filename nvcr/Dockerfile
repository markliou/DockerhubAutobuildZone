FROM nvcr.io/nvidia/tensorflow:18.02-py3
MAINTAINER markliou <markliou@ms51.url.com.tw>

RUN apt update -y;\
    apt install python3-pip -y;\
    apt install vim -y;\
    apt install git -y;\
    pip3 install --upgrade pip;\
    pip3 install tensorflow-gpu;\
    pip3 install tqdm;\
    pip3 install Pillow;\
    pip3 install scipy

# RUN mkdir /workspace
WORKDIR /workspace
    
# IPython    
EXPOSE 8888
# TensorBoard 
EXPOSE 6006   
    
CMD ["bash"]