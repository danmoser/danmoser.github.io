Title or main part
###################

.. contents:: Table of contents
    :depth: 8

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

*emphasis*, **strong** 
``literal or code``

A text with :sub:`Subscript` and :sup:`Superscript`.

:strike:`This will be crossed out.`

`Example of hiperlink <http://danmoser.github.io>`_.

Lorem ipsum [Ref]_ dolor sit amet.

.. [Ref] Book or article reference, URL or whatever.

.. code-block:: python

    import A as B
    print('B')
    for i in range(3):
        print i


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

.. note:: can be useful to emphasize important feature

.. warning:: arg2 must be non-zero."""

.. image:: ../figs/poetry_clouds_prism.jpg
    :width: 256px
    :align: center
    :alt: hdt.plottemp example

A "figure" consists of image data, an optional caption (a single paragraph), and an optional legend (arbitrary body elements). For page-based output media, figures might float to a different position if this helps the page layout.

thisis\ *one*\ word (with *emph*)!
