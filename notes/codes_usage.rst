.. role:: bash(code)
   :language: bash

Codes Usage


.. contents:: Table of contents


Hdust
########
Flags
======

=========== ========= =========== ========= ================================== =============
Compiler    FC (s)    CFLAGS (s)  FC (par)  CFLAGS (par)                       clusters
=========== ========= =========== ========= ================================== ============= 
intel       ifort     -132        mpif90    -132 -xHost -O3 -ipo -no-prec-div  acrux, lical
path_scale  pathf95   \           mpif90    -apo -Ofast                        projekct
gfortran    gfortran  \           mpif90    -O2                                acrux
=========== ========= =========== ========= ================================== =============

Computational time 
===================

============ ======== =========== ==== ================= =======
Step         n_f      time (min)  ncr  :math:`\Sigma_0`  n_proc
============ ======== =========== ==== ================= =======
1            2.5e6    1.5         ?    ?                 48
1            2.5e7    15          ?    ?                 48
1            2.0e7    53          40   ?                 48
1            7.5e8    390         40   ?                 48
5, Sob 1     5.0e6    3           ?    ?                 48
5, Sob 1     5.0e7    30          ?    ?                 48
5, Sob 0     2.0e7    2           ?    ?                 48
============ ======== =========== ==== ================= =======

Valores para teste (execução em aprox. 1 min em ``mpirun -np 3``):

- step1: 40000
- SED: 500000 (Sob 0)
- Ha: 60000 (Sob 1)


Bugs
=====
Afirmação de 17/06/2013: ``NaN`` não é um problemas de compilador ou cluster. Resultados idẽnticos no cluster projekct e na alphacrucis.

.. code::

    forrtl: severe (408): fort: (18): Dummy character variable 'MODE' has length 5 which is greater than actual variable length 1

Na versão serial: ocorre devido a flag ``-C`` na compilação.

.. code::

    forrtl: severe (71): integer divide by zero

Na versão paralela: ocorre devido a um arquivo mal especificado no input!

.. code::

    Program received signal SIGFPE: Floating point...

    Backtrace for this error:

Na versão paralela: ocorre devido a um ausência do mpirun no comando de execução!

Mesocentre
=============
Or Licallo at CRIMSON. Info at https://crimson.oca.eu/spip.php?rubrique57

.. code:: bash

    #!/bin/bash
    #OAR -n hdust_dmf
    #OAR -l /core=24,walltime=12:00:00
    #OAR -p gpu='NO'
    #OAR -O out.%jobid%
    #OAR -E err.%jobid%

    source /softs/env_default.sh
    mpiexec.hydra  -machinefile $OAR_FILE_NODES \
    -bootstrap ssh -bootstrap-exec /usr/bin/oarsh \
    -envall ./hdustparv2.02.bc input = hdust_bestar2.02.inp

The submission is

.. code:: bash

    chmod a+x job.oar
    oarsub -S ./job.oar

    oarstat

Running times
----------------
- bestar2.02, step1, 500000/24, one \.temp in 30 sec.
- bestar2.02, SED, 500000/24, one \.temp in 30 sec.

``precalcs``
==============
Run it:

.. code:: bash

    ./precalcs < dust.pre > dust.bin


Tlusty + Synspec 
###################
Tlusty: A computer program for calculating non-LTE stellar atmosphere models. The hybrid CL/ALI method + superlevels and supertransitions are treated by Opacity Distribution Functions (ODF).

To compile:

.. code:: bash

    gfortran -fno-automatic -O3 -ffixed-line-length-none -std=legacy -o tlusty200 tlusty200.f

Error in line 1365 (*Tlusty200*):

.. code::

    -* ’QTLAS ’,’ITLUCY’,’IACLT ’,’IACLDT

Synspec: a general spectrum synthesis program. It assumes an existing atmospheric model (Tlusty or Kurucz).

Synplot: a wrapper for Synspec.

Kurucz
==========
http://kurucz.harvard.edu/

Hdust uses ``ap00k1.pck``, with Solar abundances from Anders & Grevesse (1989). In this format, all models are inside a single file.

hdust.pro
===========
ilow = 2; transitions starting at Balmer series (n = ilow = 2).

Nlower = 6; it will consider the following Nlower series (ilow_max = 2+6-1 = 7).

Nupper = 12; each series above (Nlower) will have Nupper transitions.

Nlines = Nupper\Nlower; this is the total number of transitions considered.

Synspec + Synplot
====================
Arquivos necessários para rodar o synspec:

- synspec (EXE) + rotin (EXE)
- synplot.pro (IDL)
- entrada.5 ("main input"). Aqui também o ``.dat``, arquivos com as informações das transições das linhas (atom models, no site do Tlusty).
- kurucz.dat. Modelos de atm. do Kurucz - ou do Tlusty.

.. code::

    IDL > synplot49, 0, 0, 0, wsta=6530, we=6600, vrot=0, atmos=['atmos.5', $
    'ap00k1tef15000g3.0.dat'], wd=0.5, imode=2, /kurucz, x, y

    IDL > synplot49, 0, 0, 0, wsta=6530, we=6600, vrot=0, atmos=[$
    'BG15000g300v2'], wd=0.5, imode=2, x, y  ;+ nst file

fort.5 = std input; fort.8 = model.

"Bug" no synspec: se o modelo de atmosfera for de 72 (Kurucz), com ``dens=0`` ele trava (acontece no último nível de atm. Deve-se remover). 

Synspec
--------
Para compilar com o synspec com gfortran, vc precisar deixar a linha 1558 e seguinte assim:

.. code::

      IF(FINSTD.NE.BLNK)
     *   OPEN(UNIT=INPFI,FILE=FINSTD,STATUS='UNKNOWN')

(acho que é só trocar NAME por FILE).

.. code:: bash

    $ gfortran -g -fno-automatic -static -o synspec49.exe synspec49.f


VARTOOLS
###########
http://www.astro.princeton.edu/~jhartman/vartools.html

Basic/help commands
=====================
.. code:: bash

    vartools -listcommands
    vartools -help
    vartools -help $commnad
    vartools -example $command

Basic RMS
----------
:bash:`vartools -i EXAMPLES/1 -rms`

``-i $file``, input of single file

``-rms``, calculate the RMS of the lightcurve.

Basic list RMS
-------------------
:bash:`vartools -l EXAMPLES/lc_list -rms`

``-l $file``, where ``$file`` is a filename list containing the light curves, a (sub)file per line. The subfile contains a single lightcurve, 3 col: [JD, mag, errmag].

Site examples
==============
Fitting a quadratic polynomial in JD to a list of light curves
-----------------------------------------------------------------
:bash:`vartools -l EXAMPLES/lc_list -rms -decorr 1 1 1 0 1 1 2 0 -rms -chi2 -tab`

``-decorr B B B # # B``, decorrelates the light curve against specified signals
    - 0/1 enable/disable
    - 0/1 zero point term is included
    - 0/1 subtract the first term
    - 0/Nglobalterms globalfileN orderN, number of global files (files with JD and signal) + syntax
    - Nlcterms lccolumnN lcorderN, is the number of light curve specific signals. The columns of these signals are given by lccolumn1...lccolumnN. The orders of the polynomials are given by lcorder1...lcorderN.
    - 0/1 output mode, 0 our [dir]. If 1, the output contains the decorrelated signal.

``-chi2``, Calculate chi2 per dof (degree of freedom) for the light curves. The output will include chi2 and the error weighted mean magnitude.

``-tab`` format do output

Minha interpretação: 112 do final do comeando indica que só há um ajust por arquivo (1), as colunas destes sinais são as primeiras, do JD (1), e o polinômio a ser ajustado é de ordem 2 (2). Não faço ideia do pq nao se especifica os dois primeiros termos com ``-i``.

Performing a Lomb-Scargle period search on a light curve and fitting a harmonic series to the light curve
------------------------------------------------------------------------------------------------------------------------
:bash:`vartools -i EXAMPLES/2 -LS 1.0 2.0 0.01 1 0 -Killharm ls 0 0 1 EXAMPLES/OUTDIR1 -oneline`

``-LS``, Perform a Generalized Lomb-Scargle (L-S) search of the light curves for periodic sinusoidal signals. The search is done over frequencies between fmin = 1/maxp to fmax = 1/minp, with a uniform frequency step-size of Delta f = subsample/T, where T is the time-span of the observations.
    - minp maxp subsample Npeaks o(uput)periodogram

``-Killharm``, This command whitens light curves against one or more periods. The mean value of the light curve, the period of the light curve and the cos and sin coefficients are output.
    Killharm_Per1_Amplitude_1 = Max-Min
    

``-oneline``, Output each statistic on a separate line rather than using the default of outputing a table. This option can provide more readable output when processing a single light curve. It is not suggested when processing a list of light curves.


amdlib
##########
http://www.jmmc.fr/data_processing_amber.htm

Install
=========
It worked on Ubuntu 13.10 32-bits (v3.0.6+) and 14.04 64-bits (v3.0.9). Problems with Ubuntu 14.04  and (v3.0.[6-8]) (32-bits and 64-bits).

.. code:: bash

    sudo apt-get install yorick

Simply unzip the corresponding bin zip and add /path/amdlib-VERSION/bin/amdlib to your `~/.bashrc`:

.. code:: bash

    alias amdlib="$HOME/amdlib/bin/amdlib"

Running
=========
.. code::

    // Access help
    help,amdlibFunction
    // To run a script
    include,"/path/to/script.i";


``numba``
###########

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
