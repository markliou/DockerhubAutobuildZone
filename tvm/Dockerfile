# CI docker GPU env
FROM nvidia/cuda:10.1-cudnn7-devel
# FROM tensorflow/tensorflow:latest-gpu

COPY install/* /install/

# Base scripts
RUN apt-get update --fix-missing ; \
    apt upgrade -y 

RUN bash /install/ubuntu_install_core.sh ;\
    bash /install/ubuntu_install_python.sh ;\
    bash /install/ubuntu_install_python_package.sh ;\
    bash /install/ubuntu_install_llvm.sh ;\
    bash /install/ubuntu_install_opencl.sh ;\
    bash /install/ubuntu_install_sphinx.sh 

# RUN bash /install/ubuntu_install_core.sh

# COPY install/ubuntu_install_python.sh /install/ubuntu_install_python.sh
# RUN bash /install/ubuntu_install_python.sh

# COPY install/ubuntu_install_python_package.sh /install/ubuntu_install_python_package.sh
# RUN bash /install/ubuntu_install_python_package.sh

# COPY install/ubuntu_install_llvm.sh /install/ubuntu_install_llvm.sh
# RUN bash /install/ubuntu_install_llvm.sh

# COPY install/ubuntu_install_opencl.sh /install/ubuntu_install_opencl.sh
# RUN bash /install/ubuntu_install_opencl.sh

# COPY install/ubuntu_install_sphinx.sh /install/ubuntu_install_sphinx.sh
# RUN bash /install/ubuntu_install_sphinx.sh

# Enable doxygen for c++ doc build
RUN apt-get update && apt-get install -y doxygen graphviz libprotobuf-dev protobuf-compiler

RUN bash /install/ubuntu_install_java.sh ;\
    bash /install/ubuntu_install_nodejs.sh ;\
    bash /install/ubuntu_install_rocm.sh 

# COPY install/ubuntu_install_java.sh /install/ubuntu_install_java.sh
# RUN bash /install/ubuntu_install_java.sh

# COPY install/ubuntu_install_nodejs.sh /install/ubuntu_install_nodejs.sh
# RUN bash /install/ubuntu_install_nodejs.sh

# COPY install/ubuntu_install_rocm.sh /install/ubuntu_install_rocm.sh
# RUN bash /install/ubuntu_install_rocm.sh

# DL Frameworks
COPY install/* /install/
RUN bash /install/ubuntu_install_tensorflow.sh ;\
    bash /install/install_tvm_gpu.sh ;\
    bash /install/ubuntu_install_tflite.sh ;\
    bash /install/ubuntu_install_redis.sh ;\
    bash /install/ubuntu_install_redis.sh ;\
    bash /install/ubuntu_install_nnpack.sh 

RUN apt-get install -y --no-install-recommends \
    g++-arm-linux-gnueabihf gcc-arm-linux-gnueabihf \
    gcc-5-arm-linux-gnueabihf g++-5-arm-linux-gnueabihf


# COPY install/ubuntu_install_tensorflow.sh /install/ubuntu_install_tensorflow.sh
# RUN bash /install/ubuntu_install_tensorflow.sh

# COPY install/ubuntu_install_darknet.sh /install/ubuntu_install_darknet.sh
# RUN bash /install/ubuntu_install_darknet.sh

# COPY install/ubuntu_install_onnx.sh /install/ubuntu_install_onnx.sh
# RUN bash /install/ubuntu_install_onnx.sh

# COPY install/ubuntu_install_tflite.sh /install/ubuntu_install_tflite.sh
# RUN bash /install/ubuntu_install_tflite.sh

# COPY install/ubuntu_install_caffe2.sh /install/ubuntu_install_caffe2.sh
# RUN bash /install/ubuntu_install_caffe2.sh

# COPY install/ubuntu_install_dgl.sh /install/ubuntu_install_dgl.sh
# RUN bash /install/ubuntu_install_dgl.sh

# COPY install/ubuntu_install_vulkan.sh /install/ubuntu_install_vulkan.sh
# RUN bash /install/ubuntu_install_vulkan.sh

# install TVM
# COPY install/install_tvm_gpu.sh /install/install_tvm_gpu.sh
# RUN bash /install/install_tvm_gpu.sh

# AutoTVM deps
# COPY install/ubuntu_install_redis.sh /install/ubuntu_install_redis.sh
# RUN bash /install/ubuntu_install_redis.sh

# NNPACK deps
# COPY install/ubuntu_install_nnpack.sh /install/ubuntu_install_nnpack.sh
# RUN bash /install/ubuntu_install_nnpack.sh

# Environment variables
ENV PATH=/usr/local/nvidia/bin:${PATH}
ENV PATH=/usr/local/cuda/bin:${PATH}
ENV CPLUS_INCLUDE_PATH=/usr/local/cuda/include:${CPLUS_INCLUDE_PATH}
ENV C_INCLUDE_PATH=/usr/local/cuda/include:${C_INCLUDE_PATH}
ENV LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/compact:${LIBRARY_PATH}
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/compact:${LD_LIBRARY_PATH}

ENV LD_LIBRARY_PATH=/opt/rocm/lib:${LD_LIBRARY_PATH}
ENV PATH=/node_modules/.bin:${PATH}
ENV VULKAN_SDK=/usr

RUN mkdir /workspace
WORKDIR /workspace

# IPython
EXPOSE 8888
# TensorBoard
EXPOSE 6006


CMD ["bash"]
