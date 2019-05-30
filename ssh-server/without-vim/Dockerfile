FROM tensorflow/tensorflow:latest-gpu-py3
MAINTAINER markliou <markliou@ms51.url.com.tw>

RUN apt update -y;\
    apt install openssh-server -y

# change the root's password as 'root'
RUN echo 'root:root' | chpasswd && mkdir /var/run/sshd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 8888
EXPOSE 6006
CMD ["/usr/sbin/sshd","-D"]




