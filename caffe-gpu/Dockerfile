FROM nvidia/cuda:7.5-cudnn5-devel-ubuntu14.04
MAINTAINER markliou@ms51.url.com.tw

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        git \
        wget \
        vim \
        htop \
        python3-pip \
        build-essential checkinstall cmake pkg-config yasm gfortran \
        libjpeg8-dev libjasper-dev libpng12-dev \
        libtiff4-dev \
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
        python-scipy && \
    rm -rf /var/lib/apt/lists/*

ENV CAFFE_ROOT=/opt/caffe
WORKDIR $CAFFE_ROOT

# FIXME: clone a specific git tag and use ARG instead of ENV once DockerHub supports this.
ENV CLONE_TAG=master

RUN git clone -b ${CLONE_TAG} --depth 1 https://github.com/BVLC/caffe.git . && \
    for req in $(cat python/requirements.txt) pydot; do pip install $req; done && \
    mkdir build && cd build && \
    cmake -DUSE_CUDNN=1 .. && \
    make -j"$(nproc)"

ENV PYCAFFE_ROOT $CAFFE_ROOT/python
ENV PYTHONPATH $PYCAFFE_ROOT:$PYTHONPATH
ENV PATH $CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH
RUN echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig

WORKDIR /workspace
