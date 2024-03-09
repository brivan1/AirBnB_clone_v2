#!/usr/bin/python3

"""a Fabric script that generates a .tgz archive from the contents of web_static"""

import os
from datetime import datetime
from fabric.api import local

def do_pack():
    """generates a tgz archive of the directory web_static"""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    date = datetime.now()
    file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            date.year,
            date.month,
            date.day,
            date.hour,
            date.minute,
            date.second
            )
    try:
        print("archiving web_static{}".format(file_name))
        local("tar -cvzf {} web_static".format(file_name))
        size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, size))
    except Exception:
        file_name = None
    return file_name
