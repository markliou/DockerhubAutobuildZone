FROM ubuntu

MAINTAINER markliou@ms51.url.com.tw

RUN apt update -y && apt install openssh-server net-tools python ansible -y

##### setting the ssh login markliou => using "root" as user and the password is "docker"
RUN echo 'root:docker' | chpasswd && mkdir /var/run/sshd && echo "export VISIBLE=now" >> /etc/profile

RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"

#RUN echo "export VISIBLE=now" >> /etc/profile

#RUN  echo "export VISIBLE=now" >> /etc/profile
EXPOSE 22
##### end of setting ssh

#CMD /bin/bash
CMD ["/usr/sbin/sshd","-D"]
