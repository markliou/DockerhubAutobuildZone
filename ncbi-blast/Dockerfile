
FROM ubnutu

MAINTAINER markliou <markliou@ms51.url.com.tw>

RUN apt-get update && apt-get install -y --no-install-recommends \
		curl \
		python-minimal=2.7.3-4+deb7u1 \
	&& rm -rf /var/lib/apt/lists/*

# install perl and gcc
RUN apt-get install -y perl vim cpanminus make less gcc
	
# Download & install BLAST
RUN mkdir /opt/blast \
      && curl ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.6.0+-x64-linux.tar.gz \
      | tar -zxC /opt/blast --strip-components=1

# install perl module for update_blastdb.pl
RUN cpan install 

	  
ENV PATH /opt/blast/bin:$PATH



# set default behaviour
WORKDIR /blast
CMD ["bash"]