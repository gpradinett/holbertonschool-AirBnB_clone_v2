#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static.

# Install Nginx
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
# Create folders if it does not exists
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file to test Nginx - create index.html file
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create a symbolic link - If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Change ownership of user and group of /data/ folder to user: ubuntu - recursively
sudo chown -hR ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static)
sed -i "56i location /hbnb_static/ {\nalias /data/web_static/current/;\n}\n" /etc/nginx/sites-enabled/default

# Restar Nginx to make changes
sudo service nginx restart
