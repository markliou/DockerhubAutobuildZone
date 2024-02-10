#!/usr/bin/bash

export _GLIBCXX_USE_CXX11_ABI=1
export TORCH_CUDA_ARCH_LIST="8.0 8.6 8.9 9.0"

apt update -y ; apt install git cuda-toolkit-12-3  cudnn9-cuda-12 -y ; ldconfig

# install torch
echo "installing pytorch..."
cd /root
git clone --recursive https://github.com/pytorch/pytorch
cd pytorch
# if you are updating an existing checkout
git submodule sync
git submodule update --init --recursive
pip3 install cmake ninja mkl-static mkl-include
pip3 install -r requirements.txt
python setup.py bdist_wheel
# pip3 install `ls dist/*`
CUDA_HOME=/usr/local/cuda python setup.py install

# # install torch-audio
# echo "installing torch-audio..."
# cd /root
# git clone --recursive https://github.com/pytorch/audio
# cd audio
# git submodule sync
# git submodule update --init --recursive
# pip3 install -r requirements.txt
# python setup.py bdist_wheel
# # pip3 install `ls dist/*`
# python setup.py install

# # install torch-vision
# echo "installing torch-vision..."
# cd /root
# git clone --recursive https://github.com/pytorch/vision
# cd vision
# git submodule sync
# git submodule update --init --recursive
# pip3 install -r requirements.txt
# python setup.py bdist_wheel
# # pip3 install `ls dist/*`
# python setup.py install

# cleaning the folder to reduct the volume of the image
echo "cleaning the remains ..."
rm -fr /root/*
