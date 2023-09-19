#!/usr/bin/python3
# Fabfile to distribute an archive to a web server running.
from fabric.api import *
import os.path

env.hosts = ["54.144.150.9", "54.160.87.46"]


def do_deploy(archive_path):
    """Distributes an archive to a web server running.

    Args:
        archive_path (str): The path of the archive to .
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False is returned.
        Otherwise - True.
    """
    if exists(archive_path) is False:
        return False

    try:
        file_n_ed = archive_path.split("/")[-1]
        no_ext_ed = file_n_ed.split(".")[0]
        path_ed = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path_ed, no_ext_ed))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n_ed, path_ed, no_ext_ed))
        run('rm /tmp/{}'.format(file_n_ed))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path_ed, no_ext_ed))
        run('rm -rf {}{}/web_static'.format(path_ed, no_ext_ed))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path_ed, no_ext_ed))
        return True
    except:
        return False
