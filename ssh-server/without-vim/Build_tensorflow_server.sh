#!/bin/bash

server_no=5
ssh_start_port=50000

rm tensorflow-docker-server.id
for((i=0 ; i<server_no ; i++))
do
sudo docker run --rm -d -i -p $((50000+${i})):22 markliou/tensorflow-gpu-server >> tensorflow-docker-server.id
done
