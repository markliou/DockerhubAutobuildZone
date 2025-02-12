ARG TF_VER="2.18.0"
# ARG TF_VER="nightly"
ARG NV_VER="24.12-tf2-py3"

#FROM gcr.io/tensorflow/tensorflow:latest-gpu
# FROM tensorflow/tensorflow:latest-gpu-py3
# FROM tensorflow/tensorflow:1.14.0-gpu-py3
# FROM tensorflow/tensorflow:latest-gpu
# FROM tensorflow/tensorflow:1.15.0-gpu-py3
# FROM tensorflow/tensorflow:2.14.0-gpu
# FROM tensorflow/tensorflow:2.15.0-gpu #2.15 cannot use cuda#2.15 cannot use cuda
# FROM tensorflow/tensorflow:2.12.0-gpu # the pallalle dataloader can work with this version

FROM tensorflow/tensorflow:${TF_VER}-gpu
# FROM nvcr.io/nvidia/tensorflow:${NV_VER}


ENV DEBIAN_FRONTEND=noninteractive
ENV TF_FORCE_GPU_ALLOW_GROWTH=true
ENV XLA_PYTHON_CLIENT_PREALLOCATE=false
ENV XLA_PYTHON_CLIENT_ALLOCATOR=platform
ENV _GLIBCXX_USE_CXX11_ABI=1
ENV CUDA_HOME=/usr/local/cuda

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

RUN apt-get update -y;\
    apt-get install tzdata -y;\
    apt-get install python3-opencv -y --fix-missing

RUN pip install --upgrade pip

RUN apt-get update -y;\
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
    # pip3 install Flask;\
    # pip3 install futures;\
    pip3 install --upgrade keras;\
    pip3 install redis;\
    pip3 install scikit-image;\
    pip3 install tensorflow-datasets;\
    pip3 install tensorflow-addons;\
    pip3 install tensorflow-probability;\
    pip3 install matplotlib;\
    pip3 install dvc;\
    pip3 install tf-models-nightly ;\
    pip3 install opencv-contrib-python



#####  pytroch installation #####
# test the gpu available: torch.cuda.is_available()

## installing pytorch -- but skip install cuda related package
# COPY build_torch_from_source.sh /root/
# RUN /usr/bin/bash /root/build_torch_from_source.sh

## installing pytorch directly from pip
# RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

##### hugging face toolchain #####
RUN pip3 install --no-cache-dir transformers;\
    # pip3 install --no-cache-dir accelerate;\
    pip3 install --no-cache-dir -U "huggingface_hub[cli]";\
    git config --global credential.helper store


#####  jax installation #####
## installing Jax with cuda -- installed aftr torch can install newer version of cuda
# RUN pip3 install --no-cache-dir --upgrade "jax[cuda12_local]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html

## installing jax directly from pip
RUN pip install -U "jax[cuda12]"

# # fix the ldconfig promblem
# RUN mv /usr/local/lib/libtbbmalloc_proxy.so.2 /usr/local/lib/libtbbmalloc_proxy.so.2.real ;\
#     ln -s /usr/local/lib/libtbbmalloc_proxy.so.2.real /usr/local/lib/libtbbmalloc_proxy.so.2 ;\
#     mv /usr/local/lib/libtbbbind_2_0.so.3 /usr/local/lib/libtbbbind_2_0.so.3.real ;\
#     ln -s /usr/local/lib/libtbbbind_2_0.so.3.real /usr/local/lib/libtbbbind_2_0.so.3 ;\
#     mv /usr/local/lib/libtbbbind_2_5.so.3 /usr/local/lib/libtbbbind_2_5.so.3.real ;\
#     ln -s /usr/local/lib/libtbbbind_2_5.so.3.real /usr/local/lib/libtbbbind_2_5.so.3 ;\
#     mv /usr/local/lib/libtbbmalloc.so.2 /usr/local/lib/libtbbmalloc.so.2.real ;\
#     ln -s /usr/local/lib/libtbbmalloc.so.2.real /usr/local/lib/libtbbmalloc.so.2 ;\
#     mv /usr/local/lib/libtbb.so.12 /usr/local/lib/libtbb.so.12.real ;\
#     ln -s /usr/local/lib/libtbb.so.12.real /usr/local/lib/libtbb.so.12 ;\
#     mv /usr/local/lib/libtbbbind.so.3 /usr/local/lib/libtbbbind.so.3.real ;\
#     ln -s /usr/local/lib/libtbbbind.so.3.real /usr/local/lib/libtbbbind.so.3 ;\
#     mv /lib/x86_64-linux-gnu/libcudadebugger.so.1 /lib/x86_64-linux-gnu/libcudadebugger.so.1.real ;\
#     ln -s /lib/x86_64-linux-gnu/libcudadebugger.so.1.real /lib/x86_64-linux-gnu/libcudadebugger.so.1 ;\
#     mv /lib/x86_64-linux-gnu/libcuda.so.1 /lib/x86_64-linux-gnu/libcuda.so.1.real ;\
#     ln -s /lib/x86_64-linux-gnu/libcuda.so.1.real /lib/x86_64-linux-gnu/libcuda.so.1

# the gpu test script: Tensorflow, Jax, pyTorch
COPY gpu_test.py /usr/local/bin/gpu_test
RUN chmod 0755 /usr/local/bin/gpu_test

# RUN pip3 uninstall tensorflow-gpu -y;\
#     pip3 uninstall tensorflow -y;\
#     pip3 install --upgrade tensorflow-gpu==1.14

# SSH server, using "root" and password is "docker"
RUN apt-get install openssh-server -y;\
    echo 'root:docker' | chpasswd && mkdir /var/run/sshd && echo "export VISIBLE=now" >> /etc/profile ;\
    sed -i 's/\#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config ;\
    sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# VS code extensions
# RUN curl -fsSL https://code-server.dev/install.sh | sh
# RUN code-server --install-extension ms-python.python \
#                 --install-extension ms-ceintl.vscode-language-pack-zh-hant \
#                 --install-extension ms-python.debugpy \
#                 --install-extension ms-toolsai.jupyter \
#                 --install-extension ms-toolsai.jupyter-keymap \
#                 --install-extension ms-toolsai.jupyter-renderers \
#                 --install-extension ms-toolsai.vscode-jupyter-cell-tags \
#                 --install-extension ms-toolsai.vscode-jupyter-slideshow



# providing the public key for loggin (optional)
RUN mkdir /root/.ssh ;\
    touch /root/.ssh/authorized_keys ;\
    chmod 644 /root/.ssh ;\
    chmod 644 /root/.ssh/authorized_keys ;\
    echo ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDKgLR7W2eqrB3SOKbKr5wom8ZmhAPKwXiCd+H+9GKeG1uxCYPJbRoMXBG+8ot/pyyk7ObVpJvTxkPYhKkc1j2LGsgJ2O8AMo1t0PYGn0Lr5UdnxwnBjuxOZk9cRXAlfhVQkYLwRP+47+JYEHUUiuAKxxmfiuEVag8yrpw9BrB86XdR7bTqw8bAn8h1t1LYmAEc/Bh9GAWQuu7TDO0d6ymM1uygioYQrvy76mmK4zlbuVXqTLUUF5TjmJvZHjbjMDUvnr8P5DELo23VWBSP64CRLDSD3Q0l1l+X7zwuIc5H99aDg/x8txzfynjrP1P2Ae4sZBLLnaKDtZF2zaiTOJm08eFQ5x/xEByR8Lo2K590DwhGBARQStLbXtjb4B5rS9CmkE0+DWX6Mg9yrmmQmFWCNo3NTYn7xx/S56E5IYJlXdFbIO8BfAoNaLx2LdJldUklKctPyAEvtIDMCuEwVZTYwXJT7AFZ1KClp0nbP3dl20PkYQRzivWyA38SaSu7fg0= markliou@markliou-ZBPDuo >> /root/.ssh/authorized_keys

# RUN mkdir /workspace
WORKDIR /workspace

# IPython
EXPOSE 8888
# TensorBoard
EXPOSE 6006
# ssh
EXPOSE 22

CMD ["/etc/init.d/ssh", "start", "-D"]
