.. role:: strike
    :class: strike

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

Naming variables
-------------------
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

Formating printing in Python
-----------------------------
Using *%* and *.format()* for great good!

https://pyformat.info/

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

Image Filtering in Python
---------------------------
A prior: https://code.tutsplus.com/tutorials/image-filtering-in-python--cms-29202


numpy compared to R
====================

=========================== =============================
R                           numpy
=========================== =============================
a <- c(33, 44, 92, 58)      a = np.array(33, 30, 92, 58)
a[a>30]                     a(np.where(a>30))
which.max(a)                np.where(a == np.max(a))
match(30, a)                np.where(a == 30)
*no not work*: match(a,30)  *okay* np.where(30 == a)
summary(a)                  (not in numpy)

=========================== =============================

.. code::

    # R: 
    fx <- function(x) {x**2}

.. code:: python

    # Python:
    def fx(x): 
        return x**2


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
    os.path.split(observ) == (os.path.dirname(observ), os.path.basename(observ))


``input`` vs ``raw_input``
=============================
``raw_input`` does not exists in Python 3.x. It was renamed to ``input``.


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
    # OR
    python3.6 -m pip install --user pipenv

"Could not find .egg-info"
---------------------------
It is a bug, solved by `setuptools`. In Debian/Ubuntu, run

.. code:: bash

    sudo pip install pip -U
    sudo pip install setuptools -U

Setting up virtual environments 
----------------------------------
.. code:: bash

    pip freeze > requirements.txt
    pip install -r requirements.txt

which pip
-----------
Problem: ``ImportError: No module named ...``

Explanation: Your ``pip`` is probably using a different ``python`` executable.
Check it:

.. code:: bash

    head -n1 $(which pip)

Solution: you can choose to use a ``virtualenv``, or install ``pip`` using ``/usr/local/bin/python``:

.. code:: bash

    curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | /usr/local/bin/python

For more installation instructions, see http://www.pip-installer.org/en/latest/installing.html.

getting pip
-------------
To install pip, securely download https://bootstrap.pypa.io/get-pip.py

.. code:: bash

    python get-pip.py --user


ipython
==========
- `ipython` is not calling the python version I want. What should I do?

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

- `ipython` v1.0 is the most updated one for Python version equal or smaller than 2.6 ou 3.2.

- *Magic functions*: starting with `%`. ``time`` is particurlarly interesting. ``%time`` measures execution time in a **single line**. ``%%time`` measures in a **line block**.

Encoding
=============
Shebang
--------
.. code:: python

    #!/usr/bin/env python
    # -*- coding:utf-8 -*-

Smart file encoding
----------------------
For Python2 (2.6+). It also works in Python3, but it is the native behavior.

.. code:: python

    from io import open


What IDE to use for Python?
================================
This is a *religious* question.

http://stackoverflow.com/questions/81584/what-ide-to-use-for-python


Matplotlib
==========
Taking long to start
---------------------
If you are getting this message:

    /home/moser/.local/lib/python2.7/site-packages/matplotlib/font_manager.py:273: UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.
      warnings.warn('Matplotlib is building the font cache using fc-list. This may take a moment.')

erase the contents of ``mpl.get_cachedir()``. Additionally, you may need to delete ``~/.config/matplotlib`` and ``~/.cache/fontconfig``.

*ThemeChanged* error
-----------------------
.. code:: python

    can't invoke "event" command: application has been destroyed
    while executing "event generate $w <<ThemeChanged>>"
    (procedure "ttk::ThemeChanged" line 6)
    invoked from within
    "ttk::ThemeChanged"

Solution: Write this line after you import matplotlib in ipython: ``%matplotlib inline``. 

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

ANIMATIONS!!!
-----------------
Excellent post: `Data Animations With Python and MoviePy <http://zulko.github.io/blog/2014/11/29/data-animations-with-python-and-moviepy/>`_


Python GUI
==============
"Always" the first option is to use `Tkinter` because it is part of the standard Python module and runs in most of the systems. However it is not so beautiful as the `Qt` library.

If someone needs pretty graphics, interactively, one may think using `pyqtgraph` (http://www.pyqtgraph.org/).


Errors
=========
.. code:: python

    # DO NOT USE THIS!
    # import sys
    # from __future__ import print_function
    # 
    # def eprint(*args, **kwargs):
    #     print(*args, file=sys.stderr, **kwargs)

    # USE THIS:
    import warnings

    warnings.warn('Be aware of what can happen when you read this...')

    raise TypeError('A `TypeError` happened here! Program stops')

- More about ``warnings``: https://pymotw.com/2/warnings/
- Following the updated recipe, the warnings (and the errors) will be printed automatically on ``sys.stderr``
- The nuilt-in error classes are listed here: https://docs.python.org/2/library/exceptions.html
- ``raise`` by default stops the program (so does ``raise Warning('Message')`` )


VO tables
============
https://github.com/astropy/astropy/blob/master/docs/io/votable/index.rst

.. code:: python

    import astropy.io.votable as votable
    votable = votable.parse("/data/Downloads/simbad")  # xml file
    table = votable.get_first_table()
    # table  # prints the table
    data = table.array
    # data[0] will NOT work! (It is a np structured array)
    datacols = list(data.dtype.names)
    arr = np.array(data[datacols[0]])


Astropy affiliated packages
=============================
Matt Craig, has created this list of Astropy affiliated packages to help improve your experience exploring astronomy using Python. 

https://www.numfocus.org/blog/leveling-up-with-open-astronomy-astropy-affiliated-packages/


Status line (printing over the same line)
============================================
.. code:: python

    def fnPrintLine(tag, msg, cols=None, sameLine=False, align='left', flush='', full=False):
        """
        prints a formated line with a tag, message and time to the screen:
        [   TAG    ] This is a message....................................... [ 22:36:39 ]

        :author: J. Humberto
        """
        if align == 'center':
            halign = '^'
        elif align == 'right':
            halign = '>'
        else:
            halign = '<'

        if cols == None:
            try:
                cols = get_terminal_width()
                if cols < 80:
                    raise
            except:
                cols = 100

        if len(msg) > cols - 34:
            msg = textwrap.wrap(msg, width=cols - 34)
            if tag == None:
                string = '{0:^16} {1:{flush}{halign}{w}}'.format('', msg[0], w=cols - 34, halign=halign, flush=flush)
                for line in msg[1:]:
                    string += '\n{0:^18} {1:{flush}{halign}{w}}'.format('', line, w=cols - 34, halign=halign, flush=flush)
            else:
                string = '[{0:^16}] {1:{flush}{halign}{w}} [{2:^12}]'.format(tag, msg[0],                               datetime.now().strftime('%H:%M:%S'), w=cols - 34, halign=halign, flush=flush)
                for line in msg[1:]:
                    string += '\n{0:^18} {1:{flush}{halign}{w}} {2:^14}'.format('', line, '', w=cols - 34, halign=halign,
                                                                                flush=flush)

        else:
            if tag == None:
                string = '{0:^18} {1:{flush}{halign}{w}}'.format('', msg, w=cols - 34, halign=halign, flush=flush)
            else:
                string = '[{0:^16}] {1:{flush}{halign}{w}} [{2:^12}]'.format(tag, msg, datetime.now().strftime('%H:%M:%S'),
                                                                             w=cols - 34, halign=halign, flush=flush)

        if sameLine == True:
            sys.stdout.write('{} \r'.format(string))
            sys.stdout.flush()
        elif sameLine == False:
            print string
        return


Check if a variable is string
=======================================
In Python 2.x, one would do for the *s* variable

.. code:: python

    isinstance(s, basestring)

to check for str or unicode objects. In Python 3.x, it would be

.. code:: python

    isinstance(s, str)

If you're writing 2.x-and-3.x-compatible code, you'll probably want to use ``six``:

.. code:: python

    from six import string_types
    isinstance(s, string_types)



*emcee* and other nice stuff
=============================
http://eso-python.github.io/ESOPythonTutorials/ESOPythonDemoDay8_MCMC_with_emcee.html

http://eso-python.github.io/ESOPythonTutorials/

https://github.com/ESO-python/ESOPythonTutorials/tree/master/notebooks

http://www.sc.eso.org/~bdias/pycoffee/refs.html


Kernel Density Estimation in Python
====================================
Kernel density estimation is a way to estimate the probability density function (PDF) of a random variable in a non-parametric way.

- https://jakevdp.github.io/blog/2013/12/01/kernel-density-estimation/

- https://jakevdp.github.io/blog/2013/12/01/kernel-density-estimation/


Adding nice help to your program
====================================
:strike:`Use the module ``optparse`` ` (depricated).

Use ``argparse``: https://docs.python.org/2/library/argparse.html


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


Capturing the shell output in Python
=====================================
This is way easier, but only works on Unix (including Cygwin).

.. code:: python

    import commands
    print commands.getstatusoutput('wc -l file')

it returns a tuple with the (return_value, output).

https://stackoverflow.com/questions/4760215/running-shell-command-from-python-and-capturing-the-output


*regex* Python tip
====================
The **'.'' (dot)** doesn't have the original *regex* meaning with the default ``re`` in Python.

So, we need to enable it using the flag ``re.DOTALL``. Example:

.. code:: python

    outgroups = re.findall(rule, string, flags=re.DOTALL)

The ``re.DOTALL`` flag tells python to make the **'.'' (dot)** special character match all characters, including newline characters. This is very important when working with multi-line strings.

http://www.thegeekstuff.com/2014/07/advanced-python-regex/


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

Multi-threading
*****************
Definitions
===========
- *Thread*: independent process, managed by the operational system. 
- *Daemon* thread: by default, the main program waits the end of all threads before closing itself. However, this condition can be relaxed, and define the so-called "daemon threads".
- *Event*: an object to communicate event between the threads.
- *Semaphore*: an object to flux control (generally, controls the available resources, as CPUs).
- *Queue*: structure that allows safe sharing of data between threads.
- *Locking*: process that makes that threads be launched or interrupted under specific circumstances.
- *Block*: Is a kind of locking. An inactive threading, or a thread without available resources, is put to sleep in the system, until an event reactivates it or a required resource becomes available. In python, this is the standard described as ``(block=True, timeout=None)``. If timeout > 0, timeout defines the maximum allowed time that a thread can sleep before raising an exception (or error). If ``block=False`` a thread can not be put to sleep.
- *Sleep*: state of an inactive thread.

`David Beazley - Python Concurrency From the Ground Up (PyCon 2015) <https://www.youtube.com/watch?v=MCs5OvhV9S4>`_.


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


Summary
**********
.. code:: python

    # built-in functions
    for a, b in zip(list1, list2):
        ...

    mydict = dict(zip(lkeys, lvalues))
    mydict = {0: 'a', 1: 'b'}

    for i, ax in enumerate(axs):
        ...

    str1.startswith('a') or str1.endswith('z')
    print(' '.join(list1))

    datefmt = date.strftime('%Y-%m-%d')

    flines = open(file1).read().split('\n')

    os.path.split(file1) == (os.path.dirname(file1), os.path.basename(file1))
    fname_wdir, fext = os.path.splitext(file)
    fullpath = os.path.join(root, subdir, filen)
    os.path.isdir(file1)
    dircont = os.listdir('.')

    from distutils.dir_util import copy_tree, remove_tree

    set(list1) 
    np.unique(list1)

    # numpy
    np.random.seed(1234)

    cumulative = np.arange(10).cumsum()
    std = np.arange(10).std()
    mean = np.arange(10).mean()

    xx, yy = np.meshgrid(x, y)

    # matplotlib
    font = {
        'family': 'normal',
        'weight': 'bold',
        'size': 22
    }
    matplotlib.rc('font', **font)

    fig.subplots_adjust(hspace=0.01)

    ax.fig, (ax0, ax1) = plt.subplots(2, 1, sharex=True)

    fig = plt.figure()
    gs = matplotlib.gridspec.GridSpec(lins, cols)
    gs.update(hspace=0.01)

    from matplotlib.lines import Line2D
    line = [Line2D([1], [1], color='k', marker='d', ls='')]
    label = ["B"]
    ax.plot([np.NaN], [np.NaN], label='A', marker='o', ls='.-', lw=2)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles+line, labels+label, loc='best', fancybox=True, framealpha=.5,
        fontsize=8, labelspacing=0.1, ncol=2, scatterpoints=1)

    rect = matplotlib.patches.Rectangle([x0, y0, dx, dy], ec='b', fc='b', alpha=.5,
            hatch='//')
    ax.add_patch(rect)
    ax.fill_between(t, upper_bound, X, where=X>upper_bound, facecolor='b', 
        alpha=.5)

    props = dict(boxstyle='round', facecolor='wheat', alpha=.5)
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14, 
        verticalalignment='top', horizontalalignment='center', bbox=props)

    ax.locator_params(nbins=5, axis='y')
    ax.xaxis.set_major_locator(MaxNLocator(nbins=4, prune='upper|both'))
    ax.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%.0e'))
    ax.set_yticklabels(ylabs, rotation='vertical')

    ax.set_yticks(list1)
    ax.get_yticklabels()[idx].set_visible(False)
    ax.set_xticklabels([])

    from matplotlib.ticker import AutoMinorLocator
    ax.xaxis.set_minor_locator(AutoMinorLocator(2|[2,4,5]))
    ax.xaxis.set_tick_params(width=1.3, color='k', length=4, which='minor')
    ax.minorticks_on()

    ax.invert_yaxis()

    ax.axis('equal')

    ax2 = ax.twinx()
    ax2.spines['right'].set_position(('axes', 1.05))

    all(x in list1 for x in values)


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

Compiling Python
==================
Compiling Python on Ubuntu:

- Download the source from `Python website <https://www.python.org/downloads>`_
- edit the ``setup.py`` and add ``'/usr/lib/x86_64-linux-gnu'`` to the ``lib_dirs`` list:

    .. code:: python

        lib_dirs = self.compiler.library_dirs + [
                '/lib64', '/usr/lib64',
                '/lib', '/usr/lib', '/usr/lib/x86_64-linux-gnu']

        # http://stackoverflow.com/questions/10654707/no-module-named-zlib-found
  
- edit ``Modules/setup.py`` and uncomment the lines for the module CSV, socket, SSL (set ``SSL=/usr/``), curses, zlib...
- install a list of dev libraries

    .. code:: bash

        apt-get install libreadline-dev
        apt-get install libssl-dev
        apt-get install libbz2-dev
        apt-get install build-essential
        apt-get install sqlite3
        apt-get install tk-dev
        apt-get install libsqlite3-dev
        apt-get install libc6-dev
        apt-get install libgdbm-dev
        apt-get install libncurses-dev

        # http://stackoverflow.com/questions/19148564/getting-failed-to-build-these-modules-curses-curses-panel-ssl-while-instal

- If you get the following message, there is a bug with SSL. Comment all the lines with "ethod_v2" in the files ``ssl.py`` and ``_ssl.c``:

    .. code::

        "ImportError: cannot import name HTTPSHandler"


- In the end, you should get something like this:

    .. code::

        Failed to find the necessary bits to build these modules:
        _bsddb             _sqlite3           _tkinter        
        bsddb185           dl                 imageop         
        linuxaudiodev      ossaudiodev        sunaudiodev     
        To find the necessary bits, look in setup.py in detect_modules() for the module's name.


        Failed to build these modules:
        readline

- Remember: ``zlib`` and ``ssl`` modules are required for ``pip``.


``numba``
-------------
It requires ``llvm 3.7.x``. The compilation flag of the binaries at http://llvm.org are not supported on Ubuntu 14.04, so I needed to compile it.

It makes use of the ``cmake``. And it works like this:

.. code:: bash

    # sudo apt-get install cmake

    mkdir mybuiltdir
    cd mybuiltdir

    cmake path/to/llvm/source/root
    
    cmake --build .
    
    cmake -DCMAKE_INSTALL_PREFIX=$HOME/.local/ -P cmake_install.cmake
    # cmake --build . --target install

``parsl``
-------------
A Parallel Scripting Library for Python. 

http://parsl-project.org/


Python environments and references
*************************************
- http://python-notes.curiousefficiency.org/

- `What are the Most Disliked Programming Languages? <https://stackoverflow.blog/2017/10/31/disliked-programming-languages/>`_


How to clean up conda environments
====================================
https://til.hashrocket.com/posts/9ohfsktorj-squeaky-clean-anaconda-environments
https://conda.io/docs/user-guide/tasks/manage-environments.html#removing-an-environment

.. code:: bash

    conda info -e
    conda remove --name myenv —all
    conda clean -a -y


General use Python packages in Astronomy
===========================================
- PyHdust (Python tools for hdust code)
    http://astroweb.iag.usp.br/~moser/doc/

- AstroPy (community Python library for Astronomy)
    http://www.astropy.org/
    
    - AstroQuery: http://astroquery.readthedocs.org/en/latest/

    - PhotUtils: https://photutils.readthedocs.io/en/stable/

- astroplan: An Open Source Observation Planning Package in Python
    https://arxiv.org/abs/1712.09631

- SpecViz: 1D Spectral Visualization Tool
    http://specviz.readthedocs.io/

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

- PyData tools
    http://pydata.org/downloads.html

        - The Blaze Ecosystem: http://blaze.pydata.org/

- statsmodels
    http://statsmodels.sourceforge.net/

- SpectRes: A Fast Spectral Resampling Tool in Python
    https://github.com/ACCarnall/SpectRes


Python learning for astronomers
================================
- Python para zumbis
    https://www.pycursos.com/python-para-zumbis/

- Python para desenvolvedores
    http://ricardoduarte.github.io/python-para-desenvolvedores/

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

- Python Fundamentos para Análise de Dados
    https://www.datascienceacademy.com.br/public-course?courseid=python-fundamentos


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
- IPython
    http://ipython.org/
    
- The Jupyter Notebook
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
