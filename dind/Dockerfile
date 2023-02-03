FROM ubuntu:latest
MAINTAINER markliou

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
    pigz 

RUN useradd -p "123" dockremap dockremap; \
    echo 'dockremap:165536:65536' >> /etc/subuid; \ 
    echo 'dockremap:165536:65536' >> /etc/subgid

# use the rc-23
RUN wget -O 'docker.tgz' 'https://download.docker.com/linux/static/test/x86_64/docker-23.0.0-rc.3.tgz' ; \
    tar --extract \
	--file docker.tgz \
	--strip-components 1 \
	--directory /usr/local/bin/ \
	--no-same-owner \
        --exclude 'docker/docker' \
	; \
	rm docker.tgz

# install docker
RUN curl -fsSL https://get.docker.com | sh

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
RUN head -n -1 /etc/docker/daemon.json >> /etc/docker/daemon.json~ ; \
    echo "," >> /etc/docker/daemon.json~ ; \
    echo "\"insecure-registries\" : [\"http://rg.cri.lab\",\"http://127.0.0.1\"]}" >> /etc/docker/daemon.json~ ;\
    mv /etc/docker/daemon.json~ /etc/docker/daemon.json




ENV DIND_COMMIT 1f32e3c95d72a29b3eaacba156ed675dba976cb5

RUN set -eux; \
	wget -O /usr/local/bin/dind "https://raw.githubusercontent.com/docker/docker/${DIND_COMMIT}/hack/dind"; \
	chmod +x /usr/local/bin/dind

COPY dockerd-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/dockerd-entrypoint.sh

VOLUME /var/lib/docker
EXPOSE 2375 2376

ENTRYPOINT ["/usr/local/bin/dockerd-entrypoint.sh"]
CMD []


