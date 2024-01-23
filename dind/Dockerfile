FROM ubuntu:22.04

RUN apt-get update -y ;\
    apt-get install -y \ 
    sudo wget \
    btrfs-progs \
    e2fsprogs \
    iptables \
    openssl \
    xfsprogs \
    curl \ 
    vim \
    lsb-core \
    ca-certificates curl gnupg \
    supervisor \
    pigz 

RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg; \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null; \
    apt-get update -y; \
    apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin



# workround for docker v25 issue of ulimit: https://github.com/docker/cli/issues/4807
RUN \
    echo "ulimits: $(ulimit -Sn):$(ulimit -Hn)"; \
    sed -i 's/ulimit -Hn/# ulimit -Hn/g' /etc/init.d/docker; \
    service docker start; \
    rm -rf /var/cache/apt;

# # if the docker-in-docker need to access the insecured repository, add the information here
# RUN mkdir /etc/docker; echo "{\"insecure-registries\" : [\"http://rg.cri.lab\",\"http://127.0.0.1\"]}" >> /etc/docker/daemon.json

# install nvidia-docker2. This will make the wraper, so the /etc/docker/daemon.json will be made and conflect with insecure registry setting.
# We need to rewrite the daemon.json. 
RUN distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
    && curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
    && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list && \
    apt update -y ; apt install nvidia-docker2 -y

#RUN head -n -1 /etc/docker/daemon.json >> /etc/docker/daemon.json~ ; \
#    echo "," >> /etc/docker/daemon.json~ ; \
#    echo "\"insecure-registries\" : [\"http://rg.cri.lab\",\"http://127.0.0.1\"]}" >> /etc/docker/daemon.json~ ;\
#    mv /etc/docker/daemon.json~ /etc/docker/daemon.json


COPY modprobe entry.sh /usr/local/bin/
# change the dockerd as daemon with supervisord
COPY supervisord/ /etc/supervisor/conf.d/
RUN chmod +x /usr/local/bin/modprobe /usr/local/bin/entry.sh 

VOLUME /var/lib/docker
EXPOSE 2375 2376


ENTRYPOINT ["bash","/usr/local/bin/entry.sh"]
#CMD ["bash"]


