#!/bin/bash
for i in `cat tensorflow-docker-server.id`
do
sudo docker rm -f ${i}
done
rm tensorflow-docker-server.id
