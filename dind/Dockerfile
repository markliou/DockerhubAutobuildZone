FROM ubuntu:22.04

ENV RUNNER_ALLOW_RUNASROOT true

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
    bridge-utils \
    ca-certificates curl gnupg \
    supervisor \
    pigz 

# dind might be used on systems where the nf_tables kernel module isn't available. In that case,
# we need to switch over to xtables-legacy. See https://github.com/docker-library/docker/issues/463
#RUN update-alternatives --set iptables /usr/sbin/iptables-legacy ; \
#    for f in iptables iptables-save iptables-restore ip6tables ip6tables-save ip6tables-restore ; do b="/sbin/${f/tables/tables-legacy}"; "$b" --version; ln -svT "$b" "/usr/local/sbin/.iptables-legacy/$f"; done; export PATH="/usr/local/sbin/.iptables-legacy:$PATH"; iptables --version | grep legacy

# set up subuid/subgid so that "--userns-remap=default" works out-of-the-box
#RUN set -eux; \
#    addgroup dockremap; \
#    adduser dockremap dockremap; \
#    echo 'dockremap:165536:65536' >> /etc/subuid; \
#    echo 'dockremap:165536:65536' >> /etc/subgid



# docker installing process
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg; \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null; \
    apt-get update -y; \
    apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin; 
#echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf; \
#wget https://github.com/docker-library/docker/blob/d3e33ac3bc1eab5d436b7ab2981ba539ebbb7275/25/dind/dockerd-entrypoint.sh -O /usr/local/bin/dockerd-entrypoint.sh; \



# workround for docker v25 issue of ulimit: https://github.com/docker/cli/issues/4807
RUN \
    echo "ulimits: $(ulimit -Sn):$(ulimit -Hn)"; \
    sed -i 's/ulimit -Hn/# ulimit -Hn/g' /etc/init.d/docker; \
    service docker start; \
    rm -rf /var/cache/apt;

# if the docker-in-docker need to access the insecured repository, add the information here
RUN mkdir /etc/docker; echo "{\"insecure-registries\" : [\"http://rg.cri.lab\",\"http://127.0.0.1\"]}" >> /etc/docker/daemon.json

# install nvidia-docker2. This will make the wraper, so the /etc/docker/daemon.json will be made and conflect with insecure registry setting.
# We need to rewrite the daemon.json. 
RUN distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
    && curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
    && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list && \
    apt update -y ; apt install nvidia-docker2 -y

COPY modprobe entry.sh /usr/local/bin/
# change the dockerd as daemon with supervisord
COPY supervisord/ /etc/supervisor/conf.d/
RUN chmod +x /usr/local/bin/modprobe /usr/local/bin/entry.sh 

VOLUME /var/lib/docker
EXPOSE 2375 2376


ENTRYPOINT ["bash","/usr/local/bin/entry.sh"]
#CMD ["bash"]


