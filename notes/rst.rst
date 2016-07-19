reST Tips
#############

.. contents:: Table of contents

How to install
----------------
.. code:: bash
    
    # Linux (Ubuntu, Debian)
    $ sudo apt-get install python-docutils
    # MacOS
    $ sudo pip install docutils

Usage examples
---------------
.. code:: bash

    $ rst2html file.rst > file.html
    $ rst2latex file.rst > file.tex
    $ pdflatex file.tex

File example (`here`_)
-------------------------
::

    Title or main part
    ###################

    .. contents:: Table of contents
        :depth: 2

    Chapter
    **********

    Section
    =========

    Subsection
    -----------

    Subsubsection
    ^^^^^^^^^^^^^^^

    Import paragraph
    """"""""""""""""""

    Subparagraph
    ~~~~~~~~~~~~~

    .. role:: strike
        :class: strike

    .. _my-reference-label:

    Section to cross-reference
    --------------------------
    It refers to the section itself, see :ref:`my-reference-label`.

    *emphasis*, **strong** 
    ``literal or code``

    A text with :sub:`Subscript` and :sup:`Superscript`.

    :strike:`This will be crossed out.`

    `Example of hiperlink <http://danmoser.github.io>`_.
    Lorem ipsum [Ref]_ dolor sit amet.

    .. [Ref] Book or article reference, URL or whatever.

    .. code-block:: python
    .. code-block:: bash

    .. literalinclude:: example.rb
       :language: ruby
       :emphasize-lines: 12,15-18
       :linenos:

    """ Short description of the function/class, saying what it returns!

    This is a longer explanation, which may include math with latex syntax
    :math:`\alpha`.
    Then, you need to provide optional subsection ...

    **Advantages**:

     - Uses sphinx markups, which will certainly be improved in future
       version
     - Nice HTML output with the See Also, Note, Warnings directives

    :param arg1: the first value
    :param arg2: the first value
    :type arg1: int, float,...
    :type arg2: int, float,...
    :rtype: int, float
    :returns: arg1/arg2 +arg3

    :Example:

    >>> import template
    >>> a = template.MainClass1()
    >>> a.function1(1,1,1)
    2

    .. versionadded:: something new
    .. note:: can be useful to emphasize important feature
    .. seealso:: :class:`MainClass2`
    .. warning:: arg2 must be non-zero.
    .. todo:: check that arg2 is non zero.
    """

    .. image:: ../figs/poetry_clouds_prism.jpg
        :width: 512px
        :align: center
        :alt: hdt.plottemp example
        :height: 100px
        :scale: 50 %

    A "figure" consists of image data, an optional caption (a single paragraph), and an optional legend (arbitrary body elements). For page-based output media, figures might float to a different position if this helps the page layout.

    thisis\ *one*\ word (with *emph*)!

.. _`here`: example.html

Good references
------------------
- http://docutils.sourceforge.net/docs/user/rst/quickref.html
- http://sphinx-doc.org/rest.html


Advanced feature example
-------------------------
Strikethrough text in html and latex. In the document::
    
    .. role:: strike
        :class: strike

This can be applied as follows:

    ``:strike:\`This text will be crossed out.\```

Then in my css file I have an entry (html output):

.. code:: css

    .strike {
      text-decoration: line-through;
    }

Or in my extra latex file::

    \usepackage{ulem}
    \newcommand*{\DUrolestrike}{\sout}

And it is compiled as:

.. code:: bash

    $ rst2html --stylesheet=syntax.css in.rst > out.html
    $ rst2latex --stylesheet=syntax.tex in.rst > out.tex
    
Making presentations
---------------------
rst2pdf
^^^^^^^^
Create a "slides.style" to `rst2pdf`:

.. code:: css

    {"pageSetup": {
        "width": "16cm",
        "height": "10cm",
        "margin-top": "2mm",
        "margin-bottom": "0mm",
        "margin-left": ".5cm",
        "margin-right": "1cm",
        "margin-gutter": "0cm",
        "spacing-header": "2mm",
        "spacing-footer": "0mm",
        "firstTemplate": "coverPage"
      },
      "pageTemplates" : {
      "coverPage": {
        "frames": [
            ["0cm", "0cm", "100%", "100%"]
        ],
        "showHeader" : false,
        "showFooter" : true,
        "alignment": "TA_CENTER"
        },
        "cutePage": {
            "frames": [
                ["0", "0", "100%", "100%"]
            ],
            "showHeader" : false,
            "showFooter" : false
        }
      }
    }

.. code:: bash
    
    $ rst2pdf slides.rst -b1 -s slides.style
    $ rst2pdf -b2 -s a4-landscape -o path/temp.pdf slides.rst 


rst2beamer
^^^^^^^^^^^^^
.. code:: bash

    $ rst2beamer slides.rst > slides.tex
    $ pdflatex slides.tex

