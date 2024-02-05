#!/usr/bin/bash

export _GLIBCXX_USE_CXX11_ABI=1

apt update -y ; apt install git cuda-toolkit-12-3 -y

# install torch
cd /root
git clone --recursive https://github.com/pytorch/pytorch
cd pytorch
# if you are updating an existing checkout
git submodule sync
git submodule update --init --recursive
pip3 install cmake ninja mkl-static mkl-include
# pip3 install -r requirements.txt
# python setup.py bdist_wheel
# pip3 install `ls dist/*`
# python setup.py install

# install torch-audio
cd /root
git clone --recursive https://github.com/pytorch/audio
cd audio
git submodule sync
git submodule update --init --recursive
# pip3 install -r requirements.txt
# python setup.py bdist_wheel
# pip3 install `ls dist/*`
# python setup.py install

# install torch-vision
cd /root
git clone --recursive https://github.com/pytorch/vision
cd vision
git submodule sync
git submodule update --init --recursive
# pip3 install -r requirements.txt
# python setup.py bdist_wheel
# pip3 install `ls dist/*`
# python setup.py install
