#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static directory.
from datetime import datetime
import os.path
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static directory."""
    dt_ed = datetime.utcnow()
    file_ed = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt_ed.year,
                                                         dt_ed.month,
                                                         dt_ed.day,
                                                         dt_ed.hour,
                                                         dt_ed.minute,
                                                         dt_ed.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None

    if local("tar -cvzf {} web_static".format(file_ed)).failed is True:
        return None
    return (file_ed)
