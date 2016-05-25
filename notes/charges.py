#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Modified by D. Moser in 2015-06-02

import os
from glob import glob

charges = sorted(glob('figs/charge*.*'), key=os.path.getmtime)

fout = 'Charges\n##############\n\n'
for c in charges:
    fout += '.. figure:: {0}\n    :align: center\n    :height: 500\n\n'.\
        format(c)

f0 = open('charges.rst', 'w')
f0.writelines(fout)
f0.close()
