#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from glob import glob
import numpy as np
import pyhdust.tabulate as tab

__author__ = "Daniel Moser"
__email__ = "dmfaes@gmail.com"
__version__ = "v1.1"

rstfiles = glob('*.rst')
rstfiles.sort()

head = 'DMF notes\n###########\n\n'
links = '\n\n'
for i in range(len(rstfiles)):
    f = rstfiles[i].replace('.rst', '')
    rstfiles[i] = '`{0}`_'.format(f)
    links += '.. _{0}: {0}.html\n'.format(f)

ncols = 5
lr = len(rstfiles)+2
# tot = (lr // ncols + 1)*ncols - 2
lines = lr//ncols
if lr % ncols > 0:
    lines += 1
tot = lines*ncols

mid = tot/2
if lines % 2 == 0:
    mid = tot/2-ncols/2-1

rstfiles += [ '\\' for i in range(tot - lr) ]
rstfiles.insert(int(mid), '.. image:: ../figs/index2.gif')
rstfiles.insert(-int(ncols/2), '.. image:: ../figs/index3a.gif')

rf = np.array(rstfiles).reshape(-1, ncols)
f0 = open('index.rst', 'w')
f0.writelines(head)
f0.writelines(tab.tabulate(rf, tablefmt='rst'))
f0.writelines(links)
f0.close()
