FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04
MAINTAINER markliou@ms51.url.com.tw

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        git \
        wget \
        vim \
        htop \
        python3-pip \
        python3-numpy \
        python3-dev \
        build-essential checkinstall cmake pkg-config yasm gfortran \
        libjpeg8-dev libjasper-dev libpng12-dev \
        libtiff5-dev \
        libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev \
        libxine2-dev libv4l-dev \
        libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev \
        qt5-default libgtk2.0-dev libtbb-dev \
        libatlas-base-dev \
        libfaac-dev libmp3lame-dev libtheora-dev \
        libvorbis-dev libxvidcore-dev \
        libopencore-amrnb-dev libopencore-amrwb-dev \
        x264 v4l-utils \
        libatlas-base-dev \
        libboost-all-dev \
        libgflags-dev \
        libgoogle-glog-dev \
        libhdf5-serial-dev \
        libleveldb-dev \
        liblmdb-dev \
        libopencv-dev \
        libprotobuf-dev \
        libsnappy-dev \
        protobuf-compiler \
        python-dev \
        python-numpy \
        python-pip \
        python-scipy  \
        libsqlite3-dev tk-dev \
        libssl-dev openssl \
        libffi-dev \
        libncursesw5-dev libgdbm-dev libc6-dev \
        build-essential python-dev python-setuptools python-pip python-smbus && \
    rm -rf /var/lib/apt/lists/*

# solving the hdf5 lib problem
RUN cd /usr/lib/x86_64-linux-gnu && \
    ln -s libhdf5_serial.so.8.0.2 libhdf5.so && \
    ln -s libhdf5_serial_hl.so.8.0.2 libhdf5_hl.so && \
    ln -s libboost_python-py35.so libboost_python3.so 
    
ENV CAFFE_ROOT=/opt/caffe
WORKDIR $CAFFE_ROOT

RUN git clone -b ssd --depth 1 https://github.com/weiliu89/caffe.git . && \
    pip3 install setuptools && \
    pip3 install --upgrade pip==9.0.3 && \
    for req in $(cat python/requirements.txt) pydot; do pip3 install $req; done && \
    pip3 install scikit-image && \
    wget https://raw.githubusercontent.com/markliou/DockerhubAutobuildZone/master/caffe-gpu-cuda10/MakeFile.config && \
    wget https://raw.githubusercontent.com/markliou/DockerhubAutobuildZone/master/caffe-gpu-cuda10/caffe.proto && mv caffe.proto src/caffe/proto/ &&\
    wget https://raw.githubusercontent.com/markliou/DockerhubAutobuildZone/master/caffe-gpu-cuda10/prior_box_clustered.hpp && mv prior_box_clustered.hpp include/caffe/layers/ &&\
    wget https://raw.githubusercontent.com/markliou/DockerhubAutobuildZone/master/caffe-gpu-cuda10/prior_box_clustered_layer.cpp && mv prior_box_clustered_layer.cpp src/caffe/layers &&\
    wget https://raw.githubusercontent.com/markliou/DockerhubAutobuildZone/master/caffe-gpu-cuda10/solver.cpp && mv solver.cpp src/caffe/ &&\
    wget https://raw.githubusercontent.com/markliou/DockerhubAutobuildZone/master/caffe-gpu-cuda10/multibox_loss_layer.cpp && mv multibox_loss_layer.cpp src/caffe/layers/ &&\
    wget https://raw.githubusercontent.com/markliou/DockerhubAutobuildZone/master/caffe-gpu-cuda10/solver.hpp && mv solver.hpp include/caffe/ &&\
    wget https://raw.githubusercontent.com/markliou/DockerhubAutobuildZone/master/caffe-gpu-cuda10/multibox_loss_layer.hpp && mv multibox_loss_layer.hpp include/caffe/layers/ &&\
    mv MakeFile.config Makefile.config && \
    make -j10 && \
    make pycaffe 


ENV PYCAFFE_ROOT $CAFFE_ROOT/python
ENV PYTHONPATH $PYCAFFE_ROOT:$PYTHONPATH
ENV PATH $CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH
RUN echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig

WORKDIR /workspace
