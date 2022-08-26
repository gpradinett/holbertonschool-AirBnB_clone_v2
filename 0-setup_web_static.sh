#!/usr/bin/env bash
#
#

# install nginx 
sudo apt-get isntall update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
#create folders if dont exists
sudo mkdir -p /data/web_static/releases/
sudp mkdir -p /data/web_static/shared/

SRC="/etc/nginx/sites-available/default"
STATIC="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static_current/;\n\t}\n"

# creat a HTML for try or test nginx
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# create a symbolic link, if exists it should be deleted and recreated a new
sudo ln -sf "/data/web_static/releases/test/" "/data/web_static/current"

#change ownership of user and group  of folder /data/ recusively
sudo chown -R ubuntu:ubuntu "/data"

# update nginx configuration the server with the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static)
sudo sed -i "35i $STATIC" $SRC

sudo service nginx restart
service nginx reload

