#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from time import strftime

def do_pack():
    """
    function that returns the file
    else returns None
    """
    time = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p version")
        Archive_name = "versions/web_static_{}.tgz".format(time)
        local("tar -cvzf {} web_static/".format(archive_name))
        return archive_name
    except Exception:
        return None
