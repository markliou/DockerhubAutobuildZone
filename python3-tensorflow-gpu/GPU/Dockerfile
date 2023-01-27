#FROM gcr.io/tensorflow/tensorflow:latest-gpu
# FROM tensorflow/tensorflow:latest-gpu-py3
# FROM tensorflow/tensorflow:1.14.0-gpu-py3
# FROM tensorflow/tensorflow:latest-gpu
# FROM tensorflow/tensorflow:1.15.0-gpu-py3
# FROM tensorflow/tensorflow:2.7.0-gpu
FROM tensorflow/tensorflow:2.11.0-gpu

ENV DEBIAN_FRONTEND=noninteractive
ENV TF_FORCE_GPU_ALLOW_GROWTH=true

RUN apt update -y;\
    # add-apt-repository ppa:jonathonf/python-3.6 -y;\
    # apt update -y;\
    apt install tzdata -y;\
    apt install python3-opencv -y --fix-missing

# installing Jax with cuda
# RUN pip3 install jax jaxlib==0.1.61+cuda110 -f https://storage.googleapis.com/jax-releases/jax_releases.html
RUN pip install --upgrade pip
# RUN pip install --upgrade "jax[cuda111]" -f https://storage.googleapis.com/jax-releases/jax_releases.html
# RUN pip install --upgrade "jax[cuda11_cudnn82]" -f https://storage.googleapis.com/jax-releases/jax_releases.html
RUN pip install "jax[cuda]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html

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
    # pip3 install ktext;\
    pip3 install h5py;\
    pip3 install pandas;\
    pip3 install grpcio;\
    pip3 install Flask;\
    # pip3 install futures;\
    pip3 install redis;\
    pip3 install scikit-image;\
    pip3 install tensorflow-datasets;\
    pip3 install tensorflow-addons;\
    pip3 install tensorflow-probability;\
    pip3 install matplotlib;\
    pip3 install pip install opencv-contrib-python

# RUN pip3 uninstall tensorflow-gpu -y;\
#     pip3 uninstall tensorflow -y;\
#     pip3 install --upgrade tensorflow-gpu==1.14


# SSH server, using "root" and password is "docker"
RUN apt install openssh-server -y;\
    echo 'root:docker' | chpasswd && mkdir /var/run/sshd && echo "export VISIBLE=now" >> /etc/profile ;\
    sed -i 's/\#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config ;\
    sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd 

RUN mkdir /workspace
WORKDIR /workspace

# IPython
EXPOSE 8888
# TensorBoard
EXPOSE 6006
# ssh
EXPOSE 22

CMD ["/etc/init.d/ssh", "start", "-D"]
