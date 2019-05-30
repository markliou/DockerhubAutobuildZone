FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04
MAINTAINER markliou <markliou@ms51.url.com.tw>

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update -y;\
    apt upgrade -y ;\
    apt install git -y;\
    apt install vim -y;\
    apt install cmake libncurses5-dev libncursesw5-dev -y 


RUN git clone https://github.com/Syllo/nvtop.git ;\
    mkdir -p nvtop/build && cd nvtop/build ;\
    cmake .. -DNVML_RETRIEVE_HEADER_ONLINE=True;\
    make ; make install

CMD ["nvtop"]
