#FROM gcr.io/tensorflow/tensorflow:latest-gpu
# FROM tensorflow/tensorflow:latest-gpu-py3
# FROM tensorflow/tensorflow:1.14.0-gpu-py3
# FROM tensorflow/tensorflow:latest-gpu
# FROM tensorflow/tensorflow:1.15.0-gpu-py3
# FROM tensorflow/tensorflow:2.11.0-gpu
FROM tensorflow/tensorflow:2.12.0-gpu

ENV DEBIAN_FRONTEND=noninteractive
ENV TF_FORCE_GPU_ALLOW_GROWTH=true

RUN apt update -y;\
    # add-apt-repository ppa:jonathonf/python-3.6 -y;\
    # apt update -y;\
    apt install tzdata -y;\
    apt install python3-opencv -y --fix-missing

# installing Jax with cuda
RUN pip install --upgrade pip
# RUN pip install "jax[cuda]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
RUN pip install --upgrade "jax[cuda11_pip]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html

RUN apt update -y;\
    apt install python3-pip -y;\
    apt install python3-tk -y;\
    apt install git -y;\
    apt install vim -y;\
    apt install wget -y;\
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
    pip3 install dvc;\
    pip3 install pip install opencv-contrib-python

# RUN pip3 uninstall tensorflow-gpu -y;\
#     pip3 uninstall tensorflow -y;\
#     pip3 install --upgrade tensorflow-gpu==1.14


# SSH server, using "root" and password is "docker"
RUN apt install openssh-server -y;\
    echo 'root:docker' | chpasswd && mkdir /var/run/sshd && echo "export VISIBLE=now" >> /etc/profile ;\
    sed -i 's/\#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config ;\
    sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd 

# providing the public key for loggin (optional)
RUN mkdir /root/.ssh ;\
    touch /root/.ssh/authorized_keys ;\
    chmod 644 /root/.ssh ;\
    chmod 644 /root/.ssh/authorized_keys ;\
    echo ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDKgLR7W2eqrB3SOKbKr5wom8ZmhAPKwXiCd+H+9GKeG1uxCYPJbRoMXBG+8ot/pyyk7ObVpJvTxkPYhKkc1j2LGsgJ2O8AMo1t0PYGn0Lr5UdnxwnBjuxOZk9cRXAlfhVQkYLwRP+47+JYEHUUiuAKxxmfiuEVag8yrpw9BrB86XdR7bTqw8bAn8h1t1LYmAEc/Bh9GAWQuu7TDO0d6ymM1uygioYQrvy76mmK4zlbuVXqTLUUF5TjmJvZHjbjMDUvnr8P5DELo23VWBSP64CRLDSD3Q0l1l+X7zwuIc5H99aDg/x8txzfynjrP1P2Ae4sZBLLnaKDtZF2zaiTOJm08eFQ5x/xEByR8Lo2K590DwhGBARQStLbXtjb4B5rS9CmkE0+DWX6Mg9yrmmQmFWCNo3NTYn7xx/S56E5IYJlXdFbIO8BfAoNaLx2LdJldUklKctPyAEvtIDMCuEwVZTYwXJT7AFZ1KClp0nbP3dl20PkYQRzivWyA38SaSu7fg0= markliou@markliou-ZBPDuo >> /root/.ssh/authorized_keys

RUN mkdir /workspace
WORKDIR /workspace

# IPython
EXPOSE 8888
# TensorBoard
EXPOSE 6006
# ssh
EXPOSE 22

CMD ["/etc/init.d/ssh", "start", "-D"]
