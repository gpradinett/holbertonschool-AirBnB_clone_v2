#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,
using the function do_pack
"""
from fabric.api import local
import datetime


def do_pack():
    """
    function that returns the file
    else returns None
    """
    date = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    file = "versions/web_static_{}.tgz".format(date)
    print("Packing web_static to {}".format(file))
    try:
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file))
        return ("{}".format(file))
    except Exception:
        return None
