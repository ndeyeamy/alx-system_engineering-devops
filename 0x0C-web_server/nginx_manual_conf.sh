#!/bin/bash

# solving missing nginx directory and its content
sudo mkdir -p /etc/nginx
sudo touch /etc/nginx/mime.types /etc/nginx/nginx.conf 
sudo mkdir -p /etc/nginx/sites-available/ /etc/nginx/sites-enabled
sudo touch /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

# solving missing /run/nginx.pid
sudo mkdir -p /etc/systemd/system/nginx.service.d
sudo echo "[Service]\nExecStartPost=/bin/sleep 0.1\n" > /etc/systemd/system/nginx.service.d/override.conf
sudo systemctl daemon-reload
sudo systemctl restart nginx

sudo nginx -t
