#!/usr/bin/env python
# -*- coding:utf-8 -*-

from glob import glob
import numpy as np
import pyhdust.tabulate as tab

rstfiles = glob('*.rst')
rstfiles.sort()

head = 'DMF notes\n###########\n\n'
links = '\n\n'
for i in range(len(rstfiles)):
    f = rstfiles[i].replace('.rst', '')
    rstfiles[i] = '`{0}`_'.format(f)
    links += '.. _{0}: {0}.html\n'.format(f)

ncols = 5
lr = len(rstfiles)
tot = (lr // ncols + 1)*ncols - 2
rstfiles += [ '\\' for i in range(tot - lr) ]
rstfiles.insert(tot/2-ncols/2, '.. image:: figs/index2.gif')
rstfiles.insert(-(ncols/2), '.. image:: figs/index3a.gif')
# if rstfiles[-1] == '\\': 
#     rstfiles.insert(len(rstfiles)/2, '.. image:: figs/index2.gif')
#     rstfiles = rstfiles[:-1]
# else:
#     rstfiles += [ '\\' for i in range(cols-1) ]
#     rstfiles.insert((len(rstfiles)+1)/2, '.. image:: figs/index2.gif')
rf = np.array(rstfiles).reshape(-1, ncols)
f0 = open('index.rst', 'w')
f0.writelines(head)
f0.writelines(tab.tabulate(rf, tablefmt='rst'))
f0.writelines(links)
f0.close()
