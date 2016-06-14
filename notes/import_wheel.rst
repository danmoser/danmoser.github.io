``from otherswork import wheel``: looking for useful Python packages
*********************************************************************
Python is language where simplicity matters. Thus, many features are only accessible through built-in modules, called *the standard library*. Also, Python emerged from the free software principle, and new useful packages are continuously written. In this talk, I will make a (very) short introduction to Python's *standard library*, and share my experience in finding and installing packages from Python community -- biased for use in astronomy.

Modules, Packages, and all that...
===================================
- *module* is Python code file containing definitions, functions, statements...
- *package* is structure to share a set of modules.

.. code:: python

    import this

This talk was based on the `python4astronomers article <https://python4astronomers.github.io/installation/packages.html>`_: 

    - Where does Python look for modules?
    - Multiple Pythons on your computer (``virtualenv``)
    - *Anaconda* environments 

Mandatory reading: the *standard library* documentation
==========================================================
    *"Python's* standard library *is very extensive, offering a wide range of facilities..."*

    -- its docs

    https://docs.python.org/2/library/


A few examples
----------------
- time, datetime

    .. code:: python

        import time

        # Regular and 12 hour format
        print (time.strftime("%H:%M:%S"),time.strftime("%I:%M:%S"))

        # Date with full and short year
        print (time.strftime("%Y/%b/%d"), time.strftime("%y-%m-%d"))

- linecache

    .. code:: python 

        import linecache

        theline = linecache.getline(thefilepath, desired_line_number)

- collections

    .. code:: python 

        from collections import defaultdict

        dl = defaultdict(list)
        dl['a'].append(1)   

        ds = defaultdict(set)
        ds['a'].append(1)

        from collections import OrderedDict

        od = OrderedDict()
        od['a'] = 1
        od['b'] = 2
        od['c'] = 3
        od['d'] = 4

        for it in od.items():
            print(it)

- `itertools <https://docs.python.org/2/library/itertools.html>`_

- `argparse <https://docs.python.org/2/library/argparse.html>`_ 


The Python Package Index: ``PyPi`` 
====================================
    "The Python Package Index *(aka ``PyPI`` -- formerly known as the "Cheese Shop") is the preferred hub for publishing Python packages and modules. Python's standard library supports code uploads to PyPI through its ``distutils`` module."*

https://pypi.python.org or http://cheeseshop.python.org

``pip``
========
.. code:: bash

    pip install _package_
    # --user : local install (no admin rights)
    # -U or --upgrade : upgrade existing installation
    # --no-deps : no install of dependencies packages (useful for upgrade)
    # --install-option="--prefix=$PREFIX_PATH" redirects the install

``pip`` in embedded in 2.7.9+. If you have an updated version of Python and don't find it, run this command:

.. code:: bash

    python -m ensurepip


Lists of useful modules
==========================
- In its `wiki <https://wiki.python.org/moin/UsefulModules>`_, the Python Software Foundation keeps a list of useful modules. 

- `PyPi Ranking <http://pypi-ranking.info/alltime>`_ lists projects on PyPI ranked by downloads.

A few choices
---------------
- `tqdm <https://pypi.python.org/pypi/tqdm>`_

    .. code:: python

        import time
        from tqdm import tqdm

        print('# Starting something low...')
        for i in tqdm(range(5)):
            time.sleep(1)
        print('# Done!')

- `joblib <https://pythonhosted.org/joblib/>`_
- `tinyDB <http://tinydb.readthedocs.io/en/latest/>`_
- `virtualenv <https://pypi.python.org/pypi/virtualenv>`_

Packages for Science
=====================
`Keynote: State of the Tools | SciPy 2015 | Jake VanderPlas <https://www.youtube.com/watch?v=5GlNDD7qbP4>`_.

- ipython
- Numpy
- Scipy
- Matplotlib
- Pandas
- SymPy
- PyMC / emcee
- `Numba <http://numba.pydata.org/>`_

    .. code:: python

        #!/usr/bin/env python
        # -*- coding:utf-8 -*-

        import numpy as np
        from numba import jit

        size = long(1e8)


        def my_sum(size):
            result = 0.0
            for i in range(size):
                result += i
            return result

        print(my_sum(size))


        # jit decorator tells Numba to compile this function.
        # The argument types will be inferred by Numba when function is called.
        @jit
        def nb_sum(size):
            result = 0.0
            for i in range(size):
                result += i
            return result

        print(nb_sum(size))


        def np_sum(size):
            return np.sum(np.arange(size).astype(float))

        print(np_sum(size))


    .. code:: bash
    
        # running cmd
        python -m cProfile -s cumulative numba_ex.py > numba_ex.txt


Python conferences:
    - http://conference.scipy.org/
    - http://www.pycon.org/

Lists of astronomy packages
============================
- `AstroPython <http://www.astropython.org/packages/>`_
- `Comfort at 1 AU <https://oneau.wordpress.com/2010/10/02/python-for-astronomy/#a-selection-of-astronomy-libraries>`_
- `DMF personal list <http://danmoser.github.io/notes/python_astro.html#python-environments-and-references>`_


Guru Google
-----------
Google ``python blah blah`` or ``python astronomy blah blah`` works most of the time.


Remember: Python is not only functions
=======================================
List of object-oriented features that you might want to look up as you become more experienced:

- Generators
- Class-level attributes, ``classmethods``, ``staticmethods``
- Properties and accessors
- Decorators
- Metaclasses

Excellent references:

- `Popular Python recipes @ ActiveState <http://code.activestate.com/recipes/langs/python/>`_
- `Python questions @ stackoverflow <http://stackoverflow.com/questions/tagged/python>`_
- `Foum mailing list PyCoffee @ ESO <http://www.sc.eso.org/~bdias/pycoffee/forum.html>`_

Warning! Be aware of the *spirit of Python*
==============================================
**"Break free from this subtle destroyer and reclaim a life of passion and purpose"**: `The Spirit of Python <https://www.amazon.com/Spirit-Python-Exposing-Satans-Squeeze/dp/1621362205>`_.