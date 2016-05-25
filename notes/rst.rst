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
    
    Regular paragraph...
    
    - one asterisk (\*): *text* for emphasis (italics),
    - two asterisks: (\*\*) **text** for strong emphasis (boldface), and
    - backquotes (\`\`): ``text`` for code samples.

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

