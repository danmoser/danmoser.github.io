#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from glob import glob

__author__ = "Daniel Moser"
__email__ = "dmfaes@gmail.com"
__version__ = "v1.0"

charges = sorted(glob('figs/charge*.*'), key=os.path.getmtime)

fout = 'Charges\n##############\n\n'
for c in charges:
    fout += '.. figure:: {0}\n    :align: center\n    :height: 500\n\n'.\
        format(c)

f0 = open('charges.rst', 'w')
f0.writelines(fout)
f0.close()
