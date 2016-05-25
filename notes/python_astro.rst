Python and Astronomy
#######################

.. contents:: Table of contents

General tips
*************
Style Guide
=============
Python style guide are in two PEPs (Python Enhancement Proposals): 
    - `PEP 8`_ for the main text;
    - `PEP 257`_ for docstring conventions.

.. _PEP 8: https://www.python.org/dev/peps/pep-0008/
.. _PEP 257: https://www.python.org/dev/peps/pep-0257/

Highlights
------------
Class names should normally use the *CapWords* convention. 

Function names should be lowercase, with words separated by underscores as necessary to improve readability. 

*single_trailing_underscore_* : used by convention to avoid conflicts with Python keyword, e.g.

.. code:: python

    Tkinter.Toplevel(master, class_='ClassName')

You can define functions as **is_xxx** or **has_xxx** to return Boolean values.

Line continuation with strings
-------------------------------
How is the best way to spam a string over multiple lines?

Since adjacent string literals are automatically joint into a single string, you can just use the implied line continuation inside parentheses as recommended by PEP 8:

.. code:: python

    print("Why, hello there wonderful "
          "stackoverflow people!")

http://stackoverflow.com/questions/5437619/python-style-line-continuation-with-strings

How to get rid of UTF-8 BOM
------------------------------
.. code:: python

    import codecs
    f0 = open(file)
    # DO NOT WORK
    # lines = f0.read().decode('utf-8-sig').encode('utf-8')
    lines = f0.readlines()
    f0.close()
    if lines[0].startswith(codecs.BOM_UTF8):
        lines[0] = lines[0].replace(codecs.BOM_UTF8, '', 1)
    

The use of ``_`` (underscore) in Python
-------------------------------------------
``_`` has 3 main conventional uses in Python (imported from the corresponding C conventions, probably):

    #. To hold the result of the last executed statement in an interactive interpreter session. 
    #. For translation lookup in *i18n*, as in code like: ``raise forms.ValidationError(_("Please enter a correct username"))``
    #. As a general purpose "throwaway" variable name to indicate that part of a function result is being deliberately ignored, as in code like: ``label, has_label, _ = text.partition(':')``

The latter two purposes can conflict, so many folks prefer a double-underscore ``__`` as throwaway variable.

http://stackoverflow.com/questions/5893163/what-is-the-purpose-of-the-single-underscore-variable-in-python


Python ``super()`` considered super!
======================================
https://rhettinger.wordpress.com/2011/05/26/super-considered-super/


flat a double (!) nested list:
=================================
.. code:: python

    result = []
    for x in oidata.vis2:
        for item in x._vis2data:
            result.append(item)

    # is equivalent to:
    tmp2 = [item for x in oidata.vis2 for item in x._vis2data]

There is a general answer for arbitrary nested case in Python Cookbood (3rd ed).


os.path
===========
This is the right way of dealing with paths, filenames, extensions...

.. code:: python

    observ = '/media/moser/SAMSUNG2TB/interf/interf_PIO/2015/2015-11-29_SCI_alp_Eri_oidataCalibrated.fits'
    os.path.split(observ) = (os.path.dirname(observ), os.path.basename(observ))


pip
=======
Installing in a custom folder 
------------------------------
.. code:: bash

    pip install --install-option="--prefix=$PREFIX_PATH" package_name

**Important**: pip will add `/lib/pythonX.X/site-packages/` to the `$PREFIX_PATH` defined. 

In *Ureka*, this should be `$UREKA_PATH/python/`.

`pip` not found
------------------
After installing Python 2.7.9+, you need to run

.. code:: bash

    python -m ensurepip

“Could not find .egg-info" 
---------------------------
It is a bug, solved by `setuptools`. In Debian/Ubuntu, run

.. code:: bash

    sudo pip install setuptools


ipython
==========
`ipython` is not calling the python version I want. What should I do?

.. code:: bash

    # You can discover the `ipython` you are calling typing
    which ipython
    # ~/.local/bin/ipython
    
    # Then type
    cat ~/.local/bin/ipython

    # The first line tells you the python ipython is calling
    #!/usr/local/bin/python
    # You may want to change to
    #!/usr/bin/env python

Remember: `ipython` is equivalent to `python -m IPython`.


Shebang
=============
.. code:: python

    #!/usr/bin/env python
    # -*- coding:utf-8 -*-


What IDE to use for Python?
================================
This is a *religious* question.

http://stackoverflow.com/questions/81584/what-ide-to-use-for-python


Matplotlib taking long to start
================================
If you are getting this message:

    /home/moser/.local/lib/python2.7/site-packages/matplotlib/font_manager.py:273: UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.
      warnings.warn('Matplotlib is building the font cache using fc-list. This may take a moment.')

erase the contents of ``mpl.get_cachedir()``. Additionally, you may need to delete ``~/.config/matplotlib`` and ``~/.cache/fontconfig``.

``figsize``
------------
====== =============
(2,2)  272 x 200 px
(2,8)  272 x 800 px
====== =============

Bugs
------
- `eps` = no transparency.
- `pdf` = no hatches in patches.


Python GUI
==============
"Always" the first option is to use `Tkinter` because it is part of the standard Python module and runs in most of the systems. However it is not so beautiful as the `Qt` library.

If someone needs pretty graphics, interactively, one may think using `pyqtgraph` (http://www.pyqtgraph.org/).


Check if a variable is string
=======================================
In Python 2.x, one would do for the *s* variable

.. code:: python

    isinstance(s, basestring)

to check for str or unicode objects. In Python 3.x, it would be

.. code:: python

    isinstance(s, str)


*emcee* and other nice stuff
=============================
http://eso-python.github.io/ESOPythonTutorials/ESOPythonDemoDay8_MCMC_with_emcee.html

http://eso-python.github.io/ESOPythonTutorials/


Date & Time
=============
.. code:: python

    import time
    
    ## Regular and 12 hour format ##
    print (time.strftime("%H:%M:%S"),time.strftime("%I:%M:%S"))
     
    ## Date with full and short year ##
    print (time.strftime("%Y/%m/%d"), time.strftime("%y-%m-%d"))
    
=========== ==========
Directive   Meaning
=========== ==========
%a          Weekday name.
%A          Full weekday name.
%b          Abbreviated month name.
%B          Full month name.
%c          Appropriate date and time representation.
%d          Day of the month as a decimal number [01,31].
%H          Hour (24-hour clock) as a decimal number [00,23].
%I          Hour (12-hour clock) as a decimal number [01,12].
%j          Day of the year as a decimal number [001,366].
%m          Month as a decimal number [01,12].
%M          Minute as a decimal number [00,59].
%p          Equivalent of either AM or PM.
%S          Second as a decimal number [00,61].
%U          Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.
%w          Weekday as a decimal number [0(Sunday),6].
%W          Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.
%x          Appropriate date representation.
%X          Apropriate time representation.
%y          Year without century as a decimal number [00,99].
%Y          Year with century as a decimal number.
%Z          Time zone name (no characters if no time zone exists).
%%          A literal '%' character.
=========== ==========

Profile
==============
.. code:: bash

    python -m cProfile script.py
    
Broadcasting
================
.. code:: python

    import numpy as np
    from itertools import product as itprod

    a = np.arange(120.).reshape(3, 2, 5, 2, 2)
    b = np.arange(120.).reshape(3, 2, 5, 2, 2)
    fact = np.linspace(1, 1.4, 15).reshape((3, 5))

    for i, j in itprod(range(3), range(5)):
        a[i, :, j] *= fact[i, j]

    b *= fact[:, np.newaxis, :, np.newaxis, np.newaxis] 


Pandas
=======
.. code:: python

    import pandas

    df = pandas.read_csv(csvfilename, sep=',') #,header=None)
    df.values[:10,2]

    idx = df['col3'].str.contains(regex)
    subdf = df[idx]

    # Create a DataFrame and save a CSV file
    full_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
            'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
            'age': [42, 52, 36, 24, 73],
            'preTestScore': [4, 24, 31, 2, 3],
            'postTestScore': [25, 94, 57, 62, 70]}
    
    data = [['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
            ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
            [42, 52, 36, 24, 73],
            [4, 24, 31, 2, 3],
            [25, 94, 57, 62, 70]]
    
    df1 = pandas.DataFrame(data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])

    df2 = pandas.DataFrame(full_data)

    df3 = pandas.DataFrame(data)

    dfn.to_csv('filename.csv')#, sep=',', encoding='utf-8')


List of reserved words in Python
===================================

=================== =================== ========================== =======================
ArithmeticError     AssertionError      AttributeError             BaseException
BufferError         BytesWarning        DeprecationWarning         EOFError
Ellipsis            EnvironmentError    Exception                  False
FloatingPointError  FutureWarning       GeneratorExit              IOError
ImportError         ImportWarning       IndentationError           IndexError
KeyError            KeyboardInterrupt   LookupError                MemoryError
NameError           None                NotImplemented             NotImplementedError
OSError             OverflowError       PendingDeprecationWarning  ReferenceError
RuntimeError        RuntimeWarning      StandardError              StopIteration
SyntaxError         SyntaxWarning       SystemError                SystemExit
TabError            True                TypeError                  UnboundLocalError
UnicodeDecodeError  UnicodeEncodeError  UnicodeError               UnicodeTranslateError
UnicodeWarning      UserWarning         ValueError                 Warning
ZeroDivisionError   __IPYTHON__         __IPYTHON__active          __debug__
__doc__             __import__          __name__                   __package__
abs                 all                 and                        any
apply               as                  assert                     basestring
bin                 bool                break                      buffer
bytearray           bytes               callable                   chr
class               classmethod         cmp                        coerce
compile             complex             continue                   copyright
credits             def                 del                        delattr
dict                dir                 divmod                     dreload
elif                else                enumerate                  eval
except              exec                execfile                   file
filter              finally             float                      for
format              from                frozenset                  get_ipython
getattr             global              globals                    hasattr
hash                help                hex                        id
if                  import              in                         input
int                 intern              is                         isinstance
issubclass          iter                lambda                     len
license             list                locals                     long
map                 max                 memoryview                 min
next                not                 object                     oct
open                or                  ord                        pass
pow                 print               print                      property
raise               range               raw_input                  reduce
reload              repr                return                     reversed
round               set                 setattr                    slice
sorted              staticmethod        str                        sum
super               try                 tuple                      type
unichr              unicode             vars                       while
with                xrange              yield                      zip
=================== =================== ========================== =======================

Data fitting
*********************
``curve_fit``
==============
Consider errors for fitting. The solution returns the covariation matrix. Its diagnonal is the variance (the squared root, :math:`\sigma`)!!

.. code:: python

    from scipy.optimize import curve_fit

    def gauss(x, *p):
        A, mu, sigma = p
        return A*_np.exp(-(x-mu)**2/(2.*sigma**2))+1

    p0 = [1., vels[i0], 40.]
    coeff0, cov = curve_fit(gauss, x, y, p0=p0, sigma=yerr)
    
    print('# Best coefficients are:')
    print(coeff0)
    
    
``leastsq``
=============
Consider errors for fitting. The solution, however, has no errors in the parameters.

http://wiki.scipy.org/Cookbook/FittingData


*PyHdust* + ``leastsq``
========================
.. code:: python

    import pyhdust.phc as phc
    
    def polfunc(p, phi=np.linspace(0,1,21)):
        """ 
        P(phi) = P0+A cos[4 pi(phi-delt)] """
        P0, A, delt = p
        return P0+A*np.cos(4*np.pi*(phi-delt))
        
    mag = sst.BlobDiskMod()
    mag = sst.BlobDiskMod(Qis=-.348, Uis=0.040)
    
    p0 = [.0471,.021,-.17]
    p, c2r = phc.optim(p0,mag.phiobs,mag.P2,mag.sigP,polfunc)


*PyHdust* + ``curve_fit``
==========================
.. code:: python

    import pyhdust.phc as phc

    def polfunc2(phi=np.linspace(0,1,21), *p):
        """ P(phi) = P0+A cos[4 pi(phi-delt)] """
        P0, A, delt = np.array(p).flatten()
        return P0+A*np.cos(4*np.pi*(phi-delt))
        
    mag = sst.BlobDiskMod()
    mag = sst.BlobDiskMod(Qis=-.348, Uis=0.040)
    
    p0 = [.0471,.021,-.17]
    p, perr, c2r = phc.optim2(p0,mag.phiobs,mag.P2,mag.sigP,polfunc2)


Global variables
******************
One needs to declare a variable `global` in a function when one wants that function to be able to modify the global variable. If you one wants to access it, then the `global` is not needed.

.. code:: python

    def func1():
        for i in range(3):
            glob1.append(i)
    return

    def func2():
        global glob1
        for i in range(3):
            glob1+= [i]
    return

    glob1 = []
    print glob1
    func1()
    print glob1

    glob1 = []
    print glob1
    func2()
    print glob1

The program above has this exit::

    []
    [0,1,2]
    []
    [0,1,2]

But the variable can be modified without global. To go into a bit more detail on what "modify" (mutate) means: many operations that modify an object do not re-bind the variable name, and so they are all valid without declaring the name global in the function.

.. code:: python

    d = {}
    l = []
    o = type("object", (object,), {})()
    
    def valid():     # these are all valid without declaring any names global!
       d[0] = 1      # changes what's in d, but d still points to the same object
       d[0] += 1     # ditto
       d.clear()     # ditto! d is now empty but it`s still the same object!
       l.append(0)   # l is still the same list but has an additional member
       o.test = 1    # creating new attribute on o, but o is still the same object
    return
    
    
Control Flow
****************
The syntax is the ``*`` and ``**``. The names ``*args`` and ``**kwargs`` are only by convention but there's no hard requirement to use them.

You would use ``args`` when you're not sure how many arguments might be passed to your function, i.e. it allows you pass an arbitrary number of arguments to your function. For example:

.. code:: python

    >>> def print_everything(*args):
            for count, thing in enumerate(args):
    ...         print '{0}. {1}'.format(count, thing)
    ...
    >>> print_everything('apple', 'banana', 'cabbage')
    0. apple
    1. banana
    2. cabbage

Similarly, ``**kwargs`` allows you to handle named arguments that you have not defined in advance:

.. code:: python

    >>> def table_things(**kwargs):
    ...     for name, value in kwargs.items():
    ...         print '{0} = {1}'.format(name, value)
    ...
    >>> table_things(apple = 'fruit', cabbage = 'vegetable')
    cabbage = vegetable
    apple = fruit

You can use these along with named arguments too. The explicit arguments get values first and then everything else is passed to ``*args`` and ``**kwargs``. The named arguments come first in the list. For example:

.. code:: python

    def table_things(titlestring, **kwargs)

You can also use both in the same function definition but ``*args`` must occur before ``**kwargs``.

You can also use the ``*`` and ``**`` syntax when calling a function. For example:

.. code:: python

    >>> def print_three_things(a, b, c):
    ...     print 'a = {0}, b = {1}, c = {2}'.format(a,b,c)
    ...
    >>> mylist = ['aardvark', 'baboon', 'cat']
    >>> print_three_things(*mylist)
    a = aardvark, b = baboon, c = cat

As you can see in this case it takes the list (or tuple) of items and unpacks it. By this it matches them to the arguments in the function. Of course, you could have a ``*`` both in the function definition and in the function call.

Values representation and text encoding
****************************************
===== ======= ===== ===== ===============
chars   [0-1] [0-7] [0-f]  [encoding]
Base      2     8     16     text
  2      10     2      2    (*complex*)
 16    10000   20     10    (*complex*)     
 50   110010   62     32     b'2'
===== ======= ===== ===== ===============

The text representation (or association of numerical values with characters, and other text information, as spaces, end of line, etc) is complex. The first standard was the ASCII. ASCII is 8-bits encoding with fixed lenght association and no support to advanced characters. Its *printable range* has value from 32 to 126, corresponding to the characters from *space* to ~ (i.e., 95 characters). Other standards emerged to support complex characters, as the *Latin-1* and *UTF-8* - still with 8-bits (a byte), but with variable length information.

The standard text (string) written in Python 2 is in ASCII (or the binary mode!). You can specify the text in binary mode (``b'hello'``) and Py2 will consider it as a ``str`` type: you can sum the two types (``'simple ' + b'binary'``)!. 

In Python 3, the text is in UTF-8! There is a class for binary text (``bytes``), and it you not interact with the string type anymore. The ``bytes`` type in Py3 use the direct correspondence of the printable ASCII values, and use an hexadecimal escape sequência to other values.

Of course, work in ``bytes`` is much faster than with an encoding, but it is not design to work with text (but instead to **integer** values). 


Hard install reference
*************************
Start
=============
.. code:: bash

    # In ~/.bashrc
    export PYTHONPATH=$PYTHONPATH:~/pyhdust
    
    PATH=~/.local/bin/:$PATH
    
    LD_LIBRARY_PATH="$HOME/.local/lib"
    export LD_LIBRARY_PATH PATH
    
    export LDFLAGS="-L$HOME/.local/lib"
    export CPPFLAGS="-I$HOME/.local/include"
    export CXXFLAGS=$CPPFLAGS
    export CFLAGS=$CPPFLAGS
    export LD_RUN_PATH=$LD_LIBRARY_PATH
    
    $ python setup.py install --user
    $ ./configure --prefix="~/.local"

Systems
=============
MS-Windows
-------------
When dialing with binary files in Windows (e.g., *struct, xdrlib*) open/write the files with the appendix 'b' (i.e., ``rb, wb, r+b``...).

Starting at version 2.7.9, Python comes with pip!!!

Unofficial Windows Binaries for Python Extension Packages
    http://www.lfd.uci.edu/~gohlke/pythonlibs/

Random stuff
=============
.. code:: bash

    export LDFLAGS="-L$HOME/.local/lib -L/lib -L/lib64 -L$HOME/Ureka/python/lib"
    export CPPFLAGS="-I$HOME/.local/include -I/usr/include -I$HOME/Ureka/python/include"
    export CXXFLAGS=$CPPFLAGS
    export CFLAGS=$CPPFLAGS
    export LD_RUN_PATH=$LD_LIBRARY_PATH
    export PKG_CONFIG_PATH=/sto/home/moser/.local/lib/pkgconfig:$PKG_CONFIG_PATH
    
    
    # https://sourceware.org/libffi/
    # #curl -L http://github.com/atgreen/libffi/zipball/master > libffi.zip
    # #unzip libffi.zip
    # #cd atgreen-...
    wget ftp://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz
    tar xpvf libffi-3.2.1.tar.gz
    cd libffi-3.2.1
    ./configure --prefix="$HOME/.local"
    make
    make install
    
    wget http://ftp.gnome.org/pub/gnome/sources/glib/2.44/glib-2.44.0.tar.xz
    # https://developer.gnome.org/glib/
    tar xpvf glib-2.44.0.tar.xz
    cd glib-2.44.0
    export LIBFFI_CFLAGS="-I$HOME/.local/lib/libffi-3.2.1/include"
    export LIBFFI_LIBS="-L$HOME/.local/lib -lffi"
    ./configure --prefix="$HOME/.local" 
    make
    make install
    
    # http://ftp.gnome.org/pub/gnome/sources/gtk+/
    wget http://ftp.gnome.org/pub/gnome/sources/gtk+/3.16/gtk+-3.16.2.tar.xz
    tar xpvf gtk+-3.16.2.tar.xz
    cd gtk+-3.16.2
    
    
    curl -L https://github.com/geany/geany/zipball/master > geany.zip
    unzip geany.zip 
    cd geany-geany-...
    ./autogen.sh --prefix="$HOME/.local" 
    
        ### Nativo: HORRIVEL !!!
    
    export LDFLAGS="-L$HOME/.local/lib -L/lib -L/lib64"
    export CPPFLAGS="-fPIC -I$HOME/.local/include -I/usr/include"
    export CXXFLAGS=$CPPFLAGS
    export CFLAGS=$CPPFLAGS
    export LD_RUN_PATH=$LD_LIBRARY_PATH
    
    # Error URLLIB... Recompilar python com openSSL
    wget http://www.openssl.org/source/openssl-1.0.2a.tar.gz
    tar xpvf openssl-1.0.2a.tar.gz
    cd openssl-1.0.2a
    ./config --prefix="$HOME/.local"
    make
    make install
    
    wget ftp://ftp.cwru.edu/pub/bash/readline-6.3.tar.gz
    tar xpvf readline-6.3.tar.gz
    cd readline-6.3
    ./configure --prefix="$HOME/.local"
    make
    make install
    ### ERRO: *** WARNING: renaming "readline" since importing it failed: /sto/home/moser/.local/lib/libreadline.so.6: undefined symbol: PC
    
    wget https://www.python.org/ftp/python/2.7.8/Python-2.7.8.tar.xz
    wget https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tar.xz
        ### 2.7.9 Erro SSL....
    tar xpvf Python-2.7.9.tar.xz
    cd Python-2.7.9
    vim Modules/Setup.dist
    # descomentar bloco SSL; linha ~220
    # SSL=/sto/home/moser/.local
    ### adicionar diretórios setup.py; linha ~440 #Sem efeito
    ./configure --prefix="$HOME/.local"
    
    curl -L https://github.com/cython/cython/zipball/master > cython.zip
    curl -L https://github.com/numpy/numpy/zipball/master > numpy.zip
    
    Python 2.6 or 3.2:
    wget http://archive.ipython.org/release/1.0.0/ipython-1.0.0.tar.gz
    tar xpvf ipython-1.0.0.tar.gz
    
    curl -L https://github.com/spacetelescope/PyFITS/zipball/master > pyfits.zip
    
    wget https://downloads.sourceforge.net/project/matplotlib/matplotlib/matplotlib-1.4.3/matplotlib-1.4.3.tar.gz
    tar xpvf matplotlib-1.4.3.tar.gz


Python environments and references
*************************************

General use Python packages in Astronomy
===========================================
- PyHdust (Python tools for hdust code)
    http://astroweb.iag.usp.br/~moser/doc/

- AstroPy (community Python library for Astronomy)
    http://www.astropy.org/
    
    - AstroQuery: http://astroquery.readthedocs.org/en/latest/

- astLib (set of Python modules that provides some tools for research astronomers)
    http://astlib.sourceforge.net/

- PyAstronomy (collection of astronomy related packages)
    http://www.hs.uni-hamburg.de/DE/Ins/Per/Czesla/PyA/PyA/

- Astropysics 
    https://pythonhosted.org/Astropysics/

- spectral-cube
    https://github.com/radio-astro-tools/spectral-cube
    
- Trendvis
    https://github.com/matplotlib/trendvis
    
- Kapteyn package
    http://www.astro.rug.nl/software/kapteyn/

- Python time series analysis (pytseries)
    http://pytseries.sourceforge.net/

- scikit-learn (Machine Learning in Python)
    http://scikit-learn.org/stable/

- PyQt-Fit (regression toolbox in Python)
    http://pythonhosted.org/PyQt-Fit/


Python learning for astronomers
================================
- CodeCAdemy
    http://www.codecademy.com/en/tracks/python

- Coursera
    https://www.coursera.org/course/interactivepython1

- Python4astronomers
    https://python4astronomers.github.io/

- Machine learning in Python
    http://www.scipy-lectures.org/packages/scikit-learn/index.html

- Matplotlib tutorial
    http://www.labri.fr/perso/nrougier/teaching/matplotlib/#other-types-of-plots


Python distributions
======================
- Ureka\*
    http://ssb.stsci.edu/ureka/

- Anaconda
    http://continuum.io/downloads

- Enthought Canopy
    http://www.enthought.com/products/canopy/

- Python(x,y)
    http://code.google.com/p/pythonxy/

- WinPython
    http://winpython.github.io/

- Pyzo
    http://www.pyzo.org/


Python environments
======================
- ipython
    http://ipython.org/
    
- ipython Notebook
    http://ipython.org/notebook.html
    
- Geany
    http://www.geany.org/
    
- PyCharm
    http://www.jetbrains.com/pycharm/


Utilities
============
Package Index
----------------
- PyPI
    http://cheeseshop.python.org

Cookbooks
-----------
- ActiveState Python recipes
    http://code.activestate.com/recipes/langs/python/

Articles
-----------
- Survey of software use in astronomy
    http://arxiv.org/pdf/1507.03989v1.pdf

Python code revision
----------------------
- Landscape
    https://landscape.io/

Visualization tools
----------------------
- Seaborn
    https://beta.oreilly.com/learning/data-visualization-with-seaborn

- Plotly
    https://plot.ly, http://blog.plot.ly