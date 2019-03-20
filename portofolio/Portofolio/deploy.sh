#!/bin/bash

eval "$(ssh-agent -s)" &&
ssh-add -k ~/.ssh/id_rsa &&
cd /home/ubuntu/E-Commerce-FutsalZone/portofolio/Portofolio
git pull

source ~/.profile
echo "$DOCKERHUB_PASS" | sudo docker login --username $DOCKERHUB_USER --password-stdin
sudo docker stop demoooo
sudo docker rm demoooo
sudo docker rmi rizkydh/portofolio2
sudo docker run -d --name demoooo -p 5000:5000 rizkydh/portofolio2:latest

