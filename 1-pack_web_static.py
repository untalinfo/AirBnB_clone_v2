#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static folder of your
AirBnB Clone repo
"""
from fabric.api import local
from datetime import datetime


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
