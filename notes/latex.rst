Latex and typography
**********************

Latex 
###############

.. contents:: Table of contents

LaTeX for Physicists
======================
http://www.dfcd.net/articles/latex/latex.html

.. code:: latex

    % ***********************************************************
    % ******************* PHYSICS HEADER ************************
    % ***********************************************************
    % From http://www.dfcd.net/articles/latex/latex.html
    % Version 2
    \documentclass[11pt]{article} 
    \usepackage{amsmath} % AMS Math Package
    \usepackage{amsthm} % Theorem Formatting
    \usepackage{amssymb}    % Math symbols such as \mathbb
    \usepackage{graphicx} % Allows for eps images
    \usepackage{multicol} % Allows for multiple columns
    \usepackage[dvips,letterpaper,margin=0.75in,bottom=0.5in]{geometry}
     % Sets margins and page size
    \pagestyle{empty} % Removes page numbers
    \makeatletter % Need for anything that contains an @ command 
    \renewcommand{\maketitle} % Redefine maketitle to conserve space
    { \begingroup \vskip 10pt \begin{center} \large {\bf \@title}
        \vskip 10pt \large \@author \hskip 20pt \@date \end{center}
      \vskip 10pt \endgroup \setcounter{footnote}{0} }
    \makeatother % End of region containing @ commands
    \renewcommand{\labelenumi}{(\alph{enumi})} % Use letters for enumerate
    % \DeclareMathOperator{\Sample}{Sample}
    \let\vaccent=\v % rename builtin command \v{} to \vaccent{}
    \renewcommand{\v}[1]{\ensuremath{\mathbf{#1}}} % for vectors
    \newcommand{\gv}[1]{\ensuremath{\mbox{\boldmath$ #1 $}}} 
    % for vectors of Greek letters
    \newcommand{\uv}[1]{\ensuremath{\mathbf{\hat{#1}}}} % for unit vector
    \newcommand{\abs}[1]{\left| #1 \right|} % for absolute value
    \newcommand{\avg}[1]{\left< #1 \right>} % for average
    \let\underdot=\d % rename builtin command \d{} to \underdot{}
    \renewcommand{\d}[2]{\frac{d #1}{d #2}} % for derivatives
    \newcommand{\dd}[2]{\frac{d^2 #1}{d #2^2}} % for double derivatives
    \newcommand{\pd}[2]{\frac{\partial #1}{\partial #2}} 
    % for partial derivatives
    \newcommand{\pdd}[2]{\frac{\partial^2 #1}{\partial #2^2}} 
    % for double partial derivatives
    \newcommand{\pdc}[3]{\left( \frac{\partial #1}{\partial #2}
     \right)_{#3}} % for thermodynamic partial derivatives
    \newcommand{\ket}[1]{\left| #1 \right>} % for Dirac bras
    \newcommand{\bra}[1]{\left< #1 \right|} % for Dirac kets
    \newcommand{\braket}[2]{\left< #1 \vphantom{#2} \right|
     \left. #2 \vphantom{#1} \right>} % for Dirac brackets
    \newcommand{\matrixel}[3]{\left< #1 \vphantom{#2#3} \right|
     #2 \left| #3 \vphantom{#1#2} \right>} % for Dirac matrix elements
    \newcommand{\grad}[1]{\gv{\nabla} #1} % for gradient
    \let\divsymb=\div % rename builtin command \div to \divsymb
    \renewcommand{\div}[1]{\gv{\nabla} \cdot #1} % for divergence
    \newcommand{\curl}[1]{\gv{\nabla} \times #1} % for curl
    \let\baraccent=\= % rename builtin command \= to \baraccent
    \renewcommand{\=}[1]{\stackrel{#1}{=}} % for putting numbers above =
    \newtheorem{prop}{Proposition}
    \newtheorem{thm}{Theorem}[section]
    \newtheorem{lem}[thm]{Lemma}
    \theoremstyle{definition}
    \newtheorem{dfn}{Definition}
    \theoremstyle{remark}
    \newtheorem*{rmk}{Remark}

    % ***********************************************************
    % ********************** END HEADER *************************
    % ***********************************************************

Ungrouped
===========
- graphicx + pdflatex = jpg images!
- line break = `\\\\`
- Angstrom = `\\AA`
- >> = `\\gg`
- << = `\\ll`
- no date = `\\date{}` (before maketitle)

Web-tools
===========
Latex facility online:

- http://overleaf.com

Discover Latex symbol:

- http://detexify.kirelabs.org/classify.html

Write Latex online:

- https://www.codecogs.com/latex/eqneditor.php

International support and hyphenation
========================================

The command ``\usepackage[utf8]{inputenc}`` enable writing regularly. 

The command ``\usepackage[brazil]{babel}`` enables (brazillian) hyphenation (*hifenização*). 

To teach latex the hyphenation of specific words, ``\hyphenation{ exem-plo pro-ble-ma}``. 

The above commands are often associated with ``\usepackage[T1]{fontenc}``, but this do not appear to be mandatory.


Packages and definitions
===========================
Colors!
--------
.. code:: latex

    \usepackage[usenames,dvipsnames,svgnames,table]{xcolor}
    %~ \definecolor{orange}{HTML}{FF7F00}
    %~ \definecolor{green}{rgb}{0,0.6,0}
    %~ \definecolor{gray}{rgb}{0.5,0.5,0.5}
    
*Lorem ipsum*
----------------
.. code:: latex

    \usepackage{lipsum}
    \lipsum[3-56] %Paragraphs between 3 and 56
    %\lipsum[1-4] == 1 page at iagtese
    
Hyperref and links
---------------------
.. code:: latex

    \usepackage[linktocpage=true,breaklinks=true]{hyperref}
    % \usepackage[hidelinks]{hyperref}
    

Acronyms and glossary
-----------------------
.. code:: latex

    % arara: pdflatex
    % arara: makeglossaries
    % arara: pdflatex
    \documentclass{article}

    \usepackage[acronym,toc]{glossaries}
    \makeglossaries

    \newacronym{uri}{URI}{Unique Resonance Identifier}
    \newacronym{led}{LED}{light-emitting diode}
    \newacronym{eeprom}{EEPROM}{electrically TESTICLE programmable
    read-only memory}

    \glsaddall[types=\acronymtype]
    \begin{document}
    No acronyms here.

    \printglossaries

    \end{document}

Refs: 
    - https://en.wikibooks.org/wiki/LaTeX/Glossary
    - http://texblog.org/2014/01/15/glossary-and-list-of-acronyms-with-latex/
    - http://www.dickimaw-books.com/latex/thesis/html/makeglossaries.html


Insert PDF
----------------
.. code:: latex

    \usepackage{pdfpages}
    \includepdf[pages=-]{at1.pdf}
    
RSFS fonts
-------------------
Raph Smith's Formal Script font in mathematics

.. code:: latex

    \usepackage{mathrsfs}  
    $\mathscr{abcdefghijklmnopqrstuvwxyz}$  
    $\mathscr{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$
    
Commands definitions
----------------------
.. code:: latex

    \newcommand{\short}{$\sigma$\,A\,B}
    
The right usage is ``\short{}``, and not just ``\short``. If you do so, you will have spacing problems after the command!

.. code:: latex

    %~ *\mean{}*
    \def\mean#1{\left< #1 \right>}
    
Highlight source codes
--------------------------

.. code:: latex

    \usepackage{listings}

Text decorations - strikeout
-------------------------------
.. code:: latex

    \usepackage{ulem}
    \sout{Hello World}
    
    \usepackage{soul}
    \st{Hello world}

The big reason in favor of ``soul`` is that it's able to deal with line breaks and 
hyphenation.


Advanced math!
------------------
.. code:: latex

    \usepackage{amsmath}
    
Reverse *cases* in equations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code:: latex

    \newenvironment{rcases}
      {\left.\begin{aligned}}
      {\end{aligned}\right\rbrace}

Cancel
^^^^^^^^^^^^^^^^^^^
.. code:: latex

    %~ *\cancel{}*
    \usepackage[makeroom]{cancel}

Table comments!
------------------
.. code:: latex

    \usepackage[flushleft]{threeparttable}
    %~ ...
    \begin{table}[!htbp]
    \caption{Revisions}
     \begin{threeparttable}
    \centering
        \begin{tabular}{p{0.10\linewidth}
                        p{0.15\linewidth}
                        p{0.45\linewidth}
                        p{0.20\linewidth}}
        \hline
            Title 1 & Title 2 & Title 3 & Title 4          \\
        \hline
            Cell 1  & Cell 1  & Cell 3  & Cell 4 \tnote{a} \\
            Cell 1  & Cell 1  & Cell 3  & Cell 4 \tnote{b} \\
        \hline
        \end{tabular}
        \begin{tablenotes}
            \item[a] My Note.
            \item[b] My Other Note.
        \end{tablenotes}
     \end{threeparttable}
    \end{table}

Page numbering and type
-------------------------
.. code:: latex

    \pagenumbering{roman}
    \setcounter{page}{3}
    a
    \newpage
    \pagenumbering{arabic}
    b
    \end{document}

Float positioning
-------------------
.. code:: latex

    \usepackage{placeins}
    %...
    \FloatBarrier


Subfigures
============
.. code:: latex

    \usepackage{graphicx}
    \usepackage{caption}
    \usepackage{subcaption}
    
    \begin{figure}
    \centering
    \begin{subfigure}[b]{0.3\textwidth}
    \includegraphics[width=\textwidth]{gull}
    \caption{A gull}
    \label{fig:gull}
    \end{subfigure}
    ~
    %add desired spacing between images, e. g. ~, \quad, \qquad, \hfill etc.
    %(or a blank line to force the subfigure onto a new line)
    \begin{subfigure}[b]{0.3\textwidth}
    \includegraphics[width=\textwidth]{tiger}
    \caption{A tiger} \label{fig:tiger}
    \end{subfigure}
    ~
    %add desired spacing between images, e. g. ~, \quad, \qquad, \hfill etc.
    %(or a blank line to force the subfigure onto a new line)
    \begin{subfigure}[b]{0.3\textwidth}
    \includegraphics[width=\textwidth]{mouse}
    \caption{A mouse} \label{fig:mouse}
    \end{subfigure}
    
    \caption{Pictures of animals}
    \label{fig:animals}
    \end{figure}

PDF Version
==============
To generate PDF files with version 1.4:

.. code:: bash

    dvipdfmx -V 4 test.dvi
    ps2pdf -dCompatibility=1.4 test.ps

The problem with this method is that the structure of chapters do not is generated for navigation within the file.

Compact PDF
=============
To decrease PDF file size. I test and it can really deacrese the file size. But the efficiency depends on the file contents:

.. code:: bash

    gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf

    # /screen selects low-resolution output similar to the Acrobat Distiller "Screen Optimized" setting.
    # /default selects output intended to be useful across a wide variety of uses, possibly at the expense of a larger output file.
    # /ebook selects medium-resolution output similar to the Acrobat Distiller "eBook" setting.
    # /printer selects output similar to the Acrobat Distiller "Print Optimized" setting.
    #  There is a bug with the 'printer' option
    # /prepress selects output similar to Acrobat Distiller "Prepress Optimized" setting.

    gs -sDEVICE=pdfwrite -dColorConversionStrategy=/Gray -dProcessColorModel=/DeviceGray -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf 

Other possibility is to convert PDF to PS, and then PS to PDF.


Natbib
=========
Useful sheet
-------------
http://merkel.zoneo.net/Latex/natbib.php

Correction on citations (e.g., author-year-letter)
----------------------------------------------------
After running ``bibtex``, manually do the corrections editing the ``<file>.bbl`` file. Then, execute latex (or pdflatex) twice and it is done!

Use
-------
.. code:: latex

    \usepackage{natbib}

    \newcommand{\aap}{A\&A}
    \newcommand{\apj}{ApJ}
    \newcommand{\apjl}{ApJ Letters}
    \newcommand{\mnras}{MNRAS}
    \newcommand{\aapr}{A\&A Rev.}
    \newcommand{\pasp}{PASP}
    \newcommand{\araa}{Annu. Rev. Astron. Astrophys}
    \newcommand{\zap}{Zeitschrift f\"ur Astrophysik}
    \newcommand{\apss}{Astrophysics and Space Science}
    \newcommand{\aj}{Astronomical Journal}
    \newcommand{\apjs}{ApJ Supplement}
    \newcommand{\aaps}{A\&A Supplement}
    \newcommand{\pasj}{Astronomical Society of Japan}

    \bibliographystyle{apalike}  % plainnat, apj, ...
    % \renewcommand\refname{List of Publications}  % rename the Bibliography section name
    \bibliography{/home/user/file}  % file.bib path

Setting the maximum number of authors in the full reference list
-----------------------------------------------------------------
Create a custom ``.bst`` file. Find the section ``FUNCTION {format.names}`` and replace as following:

.. code:: latex

      % nameptr #1 >
      %   { namesleft #1 >
      nameptr #1 >
         {
          nameptr #3
          #1 + =
          numnames #5
          > and
            { "others" 't :=
              #1 'namesleft := }
            'skip$
          if$
          namesleft #1 >    


More info: `StackExchange <https://tex.stackexchange.com/questions/26575/bibtex-how-can-i-automatically-reduce-long-author-lists-to-xxx-et-al/26582#26582>`_

Captions
==========
The default ``\caption`` provides two arguments. The first is optional and defines what is set in the List of Tables (LoT), while the latter is mandatory and is used in the setting of the actual caption. If you don't supply the former, it's passed as equivalent to the latter.

.. code::

    \caption[<LoT entry>]{<regular caption>}

Typography
#############
Tips
=======
- Online: go sans serif.
- Verdana = Microsoft
- Lucida Grande = Mac OS
- Georgia = formal
- AVOID Times New Roman!

Letter case
-------------
https://en.wikipedia.org/wiki/Letter_case

*Start case* in the absence of spaces is called **CamelCase**.

https://en.wikipedia.org/wiki/CamelCase

General
========
Sans serif (SS)
----------------
Arial/Helvetica
Droid Sans
Aurulant Sans (OTF)

Serif (Se)
-----------
Georgia
DejaVu Serif

Monospace (Mo)
----------------
Courier
Inconsolata (fonts-inconsolata)
Terminus-font (TTF)

Latex
=======
Sans serif (SS)
----------------
Cabin(Condensed)
Comfortaa [style]
DejaVu

Serif (Se)
-----------
DejaVu Serif
CCR (Computer Concrete)

Monospace (Mo)
----------------
Inconsolata


Install OTF or TTF Ubuntu
==========================
Copy files do ``~/.fonts/``.