#!/usr/bin/python3

import os.path
from datetime import datetime
from fabric.api import local
from fabric.api import put
from fabric.api import run
from fabric.api import env
from os.path import exists, isdir

env.hosts = ['100.25.204.217', '34.227.94.234']

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
    except Exception:
        file_name = None
    return file_name

def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        fn = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, fn))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, fn))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, fn))
        run('rm -rf {}{}/web_static'.format(path, fn))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, fn))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
