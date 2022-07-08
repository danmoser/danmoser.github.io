#!/usr/bin/env python3

"""Generate an html for each ``*.rst`` file inside ``personal`` and 
``notes`` folders."""

import os
from glob import glob


home_dir = os.path.expanduser('~')
css = ["/data/Dropbox/Scripts/User/reST/my.css", 
    (f"{home_dir}/.local/lib/python3.10/site-packages/docutils/writers/"
        "html4css1/html4css1.css")]
for c in css:
    if not os.path.exists(c):
        raise SystemError(f"{css} not found!")

folders = ["personal", "notes"] 
for fo in folders:
    os.chdir(fo)
    files = glob("*.rst")
    for fi in files:
        outfi = fi.replace(".rst", ".html")
        cmd = f"rst2html5.py --stylesheet={css[0]},{css[1]} {fi} {outfi}"
        print(f"# {cmd}")
        os.system(cmd)
    os.chdir("..")
