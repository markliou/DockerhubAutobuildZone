# docker-keras - Keras in Docker with Python 3 and TensorFlow on CPU

FROM ubuntu:16.04

# install debian packages
RUN apt-get update -y &&\
    apt-get install -y software-properties-common &&\
    add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update -qq \
 && apt-get install --no-install-recommends -y \
    # install essentials
    build-essential \
    g++ \
    git \
    wget \
    openssh-client \
    # install python 3
    python3.6 \
    python3.6-dev \
    python3.6-venv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://bootstrap.pypa.io/get-pip.py &&\
    python3.6 get-pip.py &&\
    ln -s /usr/bin/python3.6 /usr/local/bin/python3
#    ln -s /usr/local/bin/pip /usr/local/bin/pip3

# manually update numpy
RUN pip3 --no-cache-dir install -U numpy==1.13.3;\
    pip3 --no-cache-dir install tqdm;\
    pip3 --no-cache-dir install Pillow;\
    pip3 --no-cache-dir install tensorflow;\
    pip3 --no-cache-dir install scipy;\
    pip3 --no-cache-dir install keras;\
    pip3 --no-cache-dir install dill;\
    pip3 --no-cache-dir install ktext;\
    pip3 --no-cache-dir install h5py;\
    pip3 --no-cache-dir install pandas;\
    pip3 --no-cache-dir install grpcio;\
    pip3 --no-cache-dir install Flask;\
    pip3 --no-cache-dir install futures;\
    pip3 --no-cache-dir install redis;\
    pip3 --no-cache-dir install matplotlib;\
    pip3 --no-cache-dir install IPython;\
    pip3 --no-cache-dir install annoy;\
    pip3 --no-cache-dir install nltk

#ARG TENSORFLOW_VERSION=1.5.0
#ARG TENSORFLOW_DEVICE=cpu
#ARG TENSORFLOW_APPEND=
#RUN pip3 --no-cache-dir install https://storage.googleapis.com/tensorflow/linux/${TENSORFLOW_DEVICE}/tensorflow${TENSORFLOW_APPEND}-${TENSORFLOW_VERSION}-cp35-cp35m-linux_x86_64.whl

#ARG KERAS_VERSION=2.1.4
#ENV KERAS_BACKEND=tensorflow
#RUN pip3 --no-cache-dir install --no-dependencies git+https://github.com/fchollet/keras.git@${KERAS_VERSION}

RUN mkdir /workspace
WORKDIR /workspace

# IPython
EXPOSE 8888
# TensorBoard
EXPOSE 6006

CMD ["bash"]
