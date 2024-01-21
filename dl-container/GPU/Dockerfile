ARG TF_VER="2.15.0"

#FROM gcr.io/tensorflow/tensorflow:latest-gpu
# FROM tensorflow/tensorflow:latest-gpu-py3
# FROM tensorflow/tensorflow:1.14.0-gpu-py3
# FROM tensorflow/tensorflow:latest-gpu
# FROM tensorflow/tensorflow:1.15.0-gpu-py3
# FROM tensorflow/tensorflow:2.14.0-gpu 
# FROM tensorflow/tensorflow:2.15.0-gpu #2.15 cannot use cuda#2.15 cannot use cuda
# FROM tensorflow/tensorflow:2.12.0-gpu # the pallalle dataloader can work with this version

FROM tensorflow/tensorflow:${TF_VER}-gpu


ENV DEBIAN_FRONTEND=noninteractive
ENV TF_FORCE_GPU_ALLOW_GROWTH=true
ENV XLA_PYTHON_CLIENT_PREALLOCATE=false
ENV XLA_PYTHON_CLIENT_ALLOCATOR=platform

# # upgrade python to 3.11 and reinstall tensorflow
# RUN python -m pip uninstall tensorflow -y;\
#     add-apt-repository ppa:deadsnakes/ppa -y &&  apt-get update -y;\
#     apt-get install python3.11 -y;\
#     update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1;\
#     update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1;\
#     apt-get install python3-pip -y ;\
#     apt-get install python3.11-distutils -y;\
#     curl -sS https://bootstrap.pypa.io/get-pip.py | python3 ;\
#     python3 -m pip install html5lib ;\
#     python3 -m pip install tensorflow

RUN apt update -y;\
    apt install tzdata -y;\
    apt install python3-opencv -y --fix-missing

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

