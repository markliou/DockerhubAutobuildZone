#FROM gcr.io/tensorflow/tensorflow:latest-gpu
# FROM tensorflow/tensorflow:latest-gpu-py3
# FROM tensorflow/tensorflow:1.14.0-gpu-py3
# FROM tensorflow/tensorflow:latest-gpu
# FROM tensorflow/tensorflow:1.15.0-gpu-py3
FROM tensorflow/tensorflow:2.4.1-gpu

ENV DEBIAN_FRONTEND=noninteractive
ENV TF_FORCE_GPU_ALLOW_GROWTH=true

RUN apt update -y;\
    # add-apt-repository ppa:jonathonf/python-3.6 -y;\
    # apt update -y;\
    apt install tzdata -y;\
    apt install python3-opencv -y --fix-missing;\
    apt install python-scipy -y
    # apt install python3.6 -y;\
    # update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 2 ;\
    # update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1 ;\
    # rm /etc/alternatives/python3;  ln -s /usr/bin/python3.6 /etc/alternatives/python3

# installing Jax with cuda
RUN pip3 install jax jaxlib==0.1.61+cuda110 -f https://storage.googleapis.com/jax-releases/jax_releases.html

RUN apt update -y;\
    apt install python3-pip -y;\
    apt install python3-tk -y;\
    apt install git -y;\
    apt install vim -y;\
    apt install -y libsm6 libxext6 ;\
    easy_install pip ;\
    pip3 install tqdm;\
    pip3 install Pillow;\
    pip3 install scipy;\
    pip3 install dill;\
    pip3 install ktext;\
    pip3 install h5py;\
    pip3 install pandas;\
    pip3 install grpcio;\
    pip3 install Flask;\
    pip3 install futures;\
    pip3 install redis;\
    pip3 install scikit-image;\
    pip3 install tensorflow-datasets;\
    pip3 install tensorflow-addons;\
    pip3 install matplotlib

# RUN pip3 uninstall tensorflow-gpu -y;\
#     pip3 uninstall tensorflow -y;\
#     pip3 install --upgrade tensorflow-gpu==1.14

RUN mkdir /workspace
WORKDIR /workspace

# IPython
EXPOSE 8888
# TensorBoard
EXPOSE 6006


CMD ["bash"]
