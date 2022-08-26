#!/usr/bin/python3
from fabric.api import local, run, put, env
import datetime
import os.path
"""creates and distributes an archive to the web servers
"""

env.hosts = [''54.160.195.20, ''18.234.171.252]


def do_pack():
    date = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    file = "versions/web_static_{}.tgz".format(date)
    print("Packing web_static to {}".format(file))
    try:
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file))
        return ("{}".format(file))
    except Exception:
        return None


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False
    ws_rs = "web_static/releases"
    ws = "web_static"
    try:
        filename = archive_path.split('/')[1]
        put("versions/{}".format(filename), "/tmp/{}".format(filename))
        run("mkdir -p /data/{}/{}".format(ws_rs, filename[:-4]))
        run("tar -xzf /tmp/{} -C /data/{}/{}/"
            .format(filename, ws_rs, filename[:-4]))
        run("rm /tmp/{}".format(filename))
        run("mv /data/{}/{}/{}/* /data/{}/{}"
            .format(ws_rs, filename[:-4], ws, ws_rs, filename[:-4]))
        run("rm -rf /data/{}/{}/{}".format(ws_rs, filename[:-4], ws))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/{}/{} /data/{}/current"
            .format(ws_rs, filename[:-4], ws))
    except Exception:
        return False


def deploy():
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

    return True
