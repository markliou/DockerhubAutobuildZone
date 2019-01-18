#FROM gcr.io/tensorflow/tensorflow:latest-gpu
FROM nvcr.io/nvidia/tensorflow:18.12-py3
MAINTAINER markliou <markliou@ms51.url.com.tw>

# RUN apt update -y;\
#     apt install software-properties-common -y

# RUN add-apt-repository ppa:jonathonf/python-3.6 -y;\
#     apt update -y;\
#     apt install python3.6 -y;\
#     update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1 ;\
#     update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2 ;\
#     rm /etc/alternatives/python3;  ln -s /usr/bin/python3.6 /etc/alternatives/python3

RUN apt update -y;\
    apt install python3-pip -y;\
    apt install python3-tk -y;\
    apt install vim -y;\
    apt install git ;\
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
    pip3 install redis;\
    pip3 install scikit-image;\
    pip3 install matplotlib


WORKDIR /workspace
    
# IPython    
EXPOSE 8888
# TensorBoard 
EXPOSE 6006   
    
CMD ["bash"]


