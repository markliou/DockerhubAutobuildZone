FROM tensorflow/tensorflow:2.7.0-gpu

ENV DEBIAN_FRONTEND=noninteractive
ENV TF_FORCE_GPU_ALLOW_GROWTH=true

RUN apt update -y;\
    apt install tzdata -y;\
    apt install python3-opencv -y --fix-missing

RUN pip install --upgrade pip

RUN apt update -y;\
    apt install python3-pip -y;\
    apt install python3-tk -y;\
    apt install git -y;\
    apt install vim wget -y;\
    apt install -y libsm6 libxext6 ;\
    pip3 install tqdm;\
    pip3 install Pillow;\
    pip3 install scipy;\
    pip3 install dill;\
    pip3 install ktext;\
    pip3 install h5py;\
    pip3 install pandas;\
    pip3 install grpcio;\
    pip3 install Flask;\
    pip3 install futures;\
    pip3 install redis;\
    pip3 install scikit-image;\
    pip3 install tensorflow-datasets;\
    pip3 install tensorflow-addons;\
    pip3 install tensorflow-probability;\
    pip3 install matplotlib;\
    pip3 install pip install opencv-contrib-python

# installing spark
ENV SPARK_VERSION=spark-3.2.1-bin-hadoop3.2
# Install OpenJDK-8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean;\
    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
RUN cd /usr/local/src ;\
    wget https://dlcdn.apache.org/spark/spark-3.2.1/${SPARK_VERSION}.tgz ;\
    tar -zxvf ${SPARK_VERSION}.tgz ;\
    echo "" >> /etc/bash.bashrc ;\
    echo "export PATH=${PATH}:/usr/local/src/${SPARK_VERSION}/sbin/:/usr/local/src/${SPARK_VERSION}/bin/" >> /etc/bash.bashrc




# SSH server, using "root" and password is "docker"
RUN apt install openssh-server -y;\
    echo 'root:docker' | chpasswd && mkdir /var/run/sshd && echo "export VISIBLE=now" >> /etc/profile ;\
    sed -i 's/\#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config ;\
    sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

RUN mkdir /workspace
WORKDIR /workspace


# SPARK
ENV SPARK_MASTER_PORT=7077 \
SPARK_MASTER_WEBUI_PORT=8080 \
SPARK_LOG_DIR=/opt/spark/logs \
SPARK_MASTER_LOG=/opt/spark/logs/spark-master.out \
SPARK_WORKER_LOG=/opt/spark/logs/spark-worker.out \
SPARK_WORKER_WEBUI_PORT=8080 \
SPARK_WORKER_PORT=7000 \
SPARK_MASTER="spark://spark-master:7077" \
SPARK_WORKLOAD="master"
EXPOSE 8080 7077 6066

# IPython
EXPOSE 8888
# TensorBoard
EXPOSE 6006
# ssh
EXPOSE 22

CMD ["bash"]
