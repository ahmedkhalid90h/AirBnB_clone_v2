#!/usr/bin/env bash
# Sets up a web server for deployment of web_static files.

sudo apt-get -y update
sudo apt-get -y upgrade

sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

echo "Holberton School" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current


sudo chown -hR ubuntu:ubuntu /data/

sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

service nginx restart
