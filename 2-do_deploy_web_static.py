#!/usr/bin/python3
"""
distributes an archive to your web servers, using the function do_deploy
"""
from fabric.api import *
from datetime import datetime
import os.path


env.hosts = ['34.75.244.196', '54.85.50.33']


def do_pack():
    """
    creation version pack
    """
    try:
        date_format = "%Y%m%d%H%M%S"
        date = datetime.now()
        create = date.strftime(date_format)
        local("mkdir -p versions")
        fileTgz = "web_static_{}.tgz".format(create)
        local("tar -cvzf versions/{} web_static".format(fileTgz))
        return fileTgz
    except:
        return None


def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    """
    if os.path.isfile(archive_path) is False:
        return False

    try:
        put(archive_path, '/tmp/')
        folder = "/data/web_static/releases/"
        id_split = archive_path.split("_")
        my_id = id_split[2][:-4]
        run("mkdir -p {}web_static_{}/".format(folder, my_id))
        run("tar -xzf /tmp/web_static_{}.tgz -C {}web_static_{}/"
            .format(my_id, folder, my_id))
        run("rm /tmp/web_static_{}.tgz".format(my_id))
        run("mv {}web_static_{}/web_static/* {}web_static_{}/"
            .format(folder, my_id, folder, my_id))
        run("rm -rf {}web_static_{}/web_static".format(folder, my_id))
        run("rm -rf /data/web_static/current")
        run("ln -s {}web_static_{}/ /data/web_static/current"
            .format(folder, my_id))
        return True
    except:
        return False
