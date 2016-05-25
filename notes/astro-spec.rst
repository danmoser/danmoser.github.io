Tutorial de redução de dados de espectroscopia do OPD/LNA
###########################################################

.. contents:: Índice


Resumo 2016-03-28
*******************
Farei uma demonstração prática de como reduzir dados de espectroscopia de dois espectrógrafos do OPD/LNA: (i) o espectrógrafo de fenda longa Cassegrain (ECASS) e (ii) o espectrógrafo echelle MUSICOS. Para ambos os espectrógrafos serão empregadas rotinas IRAF complementadas com rotinas Python. E para o MUSICOS também executarei o software de redução OPERA, adaptado ao instrumento numa parceria do LNA com o CFHT (software utilizado no espectrógrafo ESPaDOnS).

A ideia é que o participantes tragam seus notebooks e executem simultaneamente o processo de redução na execução comentada que farei. Para isso é preciso baixar os dados de exemplo disponibilizados e ter os aplicativos já instalados. O tempo programado para as demonstrações é de 1h30.

Mais instruções no sítio http://j.mp/opdspec


Para a execução
******************
Softwares necessários para o tutorial:

- IRAF v2.16+
- pacote `beacon-reduc`
- OPERA v1.0+ com pipeline MUSICOS
- Python 2.7.5+
- Módulos Python `pyfits`, `jdcal`, `matplotlib`, `astropy`


Dados de exemplo
==================
    http://dl.dropbox.com/u/6569986/transfer/specdata.zip


Download softwares
=========================
Todos os softwares necessários encontram-se no conjunto Ureka (Mac and Linux) do Gemini Observatory e STSCI, (com exceção do OPERA). Recomendamos todos os participantes a instalarem este conjunto. O **Ureka necessita de 5.5 GB** de espaço em disco.

    http://ssb.stsci.edu/ureka/

O pacote de redução `beacon` recomenda-se o download pelo `git`:

.. code:: bash

    git clone https://github.com/danmoser/beacon.git 

E o software OPERA com o módulo do Musicos

    http://dl.dropbox.com/u/6569986/transfer/opera-1.0_ForMUSICOS-OES_2016-03-22.zip


Instalação
===========
Ureka
---------
Se você tiver um Linux 64 bits das versões abaixo, o primeiro passo é instalar os pacotes:

- Ubuntu 12.04

.. code:: bash
    
    sudo apt-get install ia32-libs

- Ubuntu 13.10, 14.04 e 14.10

.. code:: bash
    
    sudo apt-get install lib32z1 lib32ncurses5 lib32bz2-1.0

- Fedora 17, 18, 19, 20 e 21:

.. code:: bash
    
    su
    yum install glibc.i686
    yum install ncurses-libs.i686

- Debian 7:

.. code:: bash
    
    su
    dpkg --add-architecture i386
    apt-get update


Para instalar o Ureka propriamente:

.. code:: bash

    # Choose an installation directory and download this installer 
    # Run the installer by typing
    sh install_ureka_1.5.2
    
    # The installer will ask for permission to edit your login scripts. If you have 
    # more than one Ureka installation, the installer will also ask you to provide 
    # an installation name.
    # If this is your first time installing Ureka:
    source ~/.bashrc

    # To select the Ureka environment, type
    ur_setup

    # If this is the first time you run IRAF, you need to configure it
    # A file `login.cl` will contain this information
    mkiraf
    # choose xgterm
    xgterm -sb -e "cl" 

Erro `xgterm`
^^^^^^^^^^^^^^^
Em alguns casos, o `xgterm` parece não funcionar em sistemas 64 bits (erros de biblioteca). Se isso acontecer, vc pode fazer seguinte

.. code:: bash

    sudo apt-get install libuuid1:i386 libx11-xcb-dev:i386 libx11-xcb1:i386
    mv $HOME/Ureka/iraf/lib32/lib/libX11.so.6 $HOME/Ureka/iraf/lib32/lib/libX11.so.6.bkp 


OPERA
--------
OPERA depende de uma lista de softwares. Verifique no arquivo *DEPENDENCIES* após o download do programa. Alguns que destacamos: *gcc*, *cfitsio*, *fftw3*. Recomenda-se também o *gnuplot* (e *Xcode*, *Autotools* para usuários Mac).

Para instalar estas dependências no Ubuntu 14.04:

.. code:: bash

    sudo apt-get install fftw3 libfftw3-dev libcfitsio3-dev gnuplot  

Atenção: **não instale o OPERA com previlégios root**.

.. code:: bash
    
    # O código abaixo supõem a instalação na pasta `$HOME`. 
    # Substitua-o caso instale escolha outro diretório.
    cd $HOME
    rm -rf opera-1.0
    unzip opera-1.0________.zip
    cd opera-1.0
    ./configure --prefix=$HOME/opera-1.0/
    # Se quiser apagar uma instalacao anterior
    # make distclean
    make
    make install
    # . ./setup.sh

    # Instale o pipeline do MUSICOS e adicione ao PATH
    chmod +x $HOME/opera-1.0/pipeline/pyMusicos/*.py
    nano $HOME/.bashrc
    # PATH=$PATH:$HOME/opera-1.0/bin/:$HOME/opera-1.0/pipeline/pyMusicos/
    source $HOME/.bashrc

Problemas com OPERA
^^^^^^^^^^^^^^^^^^^^
1. O OPERA precisa do CFITSIO <= v3.29.


2. Dependendo do que você tinha no sistema, pode encontrar o seguinte erro:

.. code:: bash

    ERROR: Mismatch in the version of the fitsio.h include file used to build
    the CFITSIO library, and the version included by the application program:
       Version used to build the CFITSIO library   = 3.340000
       Version included by the application program = 3.290000

Este erro surgiu na minha máquina pois eu compilei e instalei como `sudo` o cfitsio v3.29, e depois instalei o cfitsio do Ubuntu (v3.34). A biblioteca vai tentar ser instalada na pasta `/usr/local/`, enquanto que o padrão Ubuntu é `/usr/`. O problema é que na compilação do OPERA esses caminhos se misturam e dá o erro acima.

Para desinstalar, eu fiz o seguinte: fui na pasta compilada e ``make distclean``. Também, verifique a existência dos seguintes arquivos:

.. code:: bash

    /usr/local/include/fitsio.h
    /usr/local/include/fitsio2.h
    /usr/local/include/drvrsmem.h
    /usr/local/include/longnam.h
    /usr/local/lib/pkgconfig/cfitsio.pc
    /usr/local/lib/libcfitsio.a



`beacon-reduc`
----------------
Pacotes IRAF por padrão são instalados na subpasta `extern`.

.. code:: bash

    # O código abaixo supõem a instalação do UREKA na pasta `$HOME`. 
    # Substitua-o caso instale escolha outro diretório.
    cd $HOME
    cd Ureka/iraf/extern
    git clone https://github.com/danmoser/beacon.git 
    
    # Caso não tenha o git instalado, pode ser feito a sequencia abaixo
    # curl -L https://github.com/danmoser/beacon/zipball/master > beacon.zip
    # unzip beacon.zip
    # mv danmoser-beacon-d517c82 beacon

    # A seguir é necessário declarar o pacote no IRAF
    nano ../../unix/hlib/extern.pkg
    # E em algum lugar antes da palavra keep, adicionar:
    # reset beacon    = iraf$extern/beacon/
    # task beacon.pkg = beacon$beacon.cl

    # O último passo eh adicionar a pasta de executáveis do pacote no PATH 
    # do shell do sistema. Editando o arquivo .bashrc:
    nano $HOME/.bashrc
    # e adicionando a linha
    # PATH=$PATH:$HOME/Ureka/iraf/extern/scripts/
    chmod +x $HOME/Ureka/iraf/extern/scripts/*
    source $HOME/.bashrc


Download e instalação alternativa
==================================
Para a instalação dos aplicativos individualmente, seguem os links:

- IRAF: http://iraf.noao.edu/
- Python: https://www.python.org/downloads/

Recomenda-se a instalação dos módulos Python através do comando ``pip`` (apropriado a cada sistema, e nativo a partir do Python 2.7.9. Na dúvida, instale uma versão atualizada do Python para obtê-lo). 

.. code:: bash

    sudo pip install pyfits
    sudo pip install matplotlib


Redução
*********
Pré-processamento
===================
#. Rodar ``create_ut.py`` para correção da velocidade heliocêntrica com o IRAF.
#. Verificar formato das imagens com ``imhead -l``.
#. Efetuar correção de cubo (modo *Kinetic* do CCD) com ``read3Dfits``.

ECASS
=========
Estrutura de pastas e arquivos
--------------------------------
NOITE/alvos, com calibrações em *calib*. Formato *bias_0x* e *flat_f_0x*, onde *f* é o respectivo flat-field (necessário a cada ângulo de posicionamento da rede).

Na pasta de **cada alvo** deve haver uma lâmpada da forma *alvo_lamp_f*. Alvo formato *alvo_f_0x*.

Passos
-------
#. Rodar na pasta de calibrações

    .. code:: bash

        epar calib_spec

#. Rodar na pasta do alvo

    .. code:: bash

        epar calib_spec

Para economizar tempo, é possível copiar a solução das linhas da lâmpada de calibração.

MUSICOS com IRAF
===================
NOITE/alvos, com calibrações em *calib*. Formato *bias_0x* e *flat_f_0x*, onde *f* é o respectivo flat-field (recomendado a cada posicionamento da rede).

So há uma lâmpada por posicionamento da rede, que deve ficar na **pasta de calibrações**. Precisa ser da forma *lamp_f_0x*.

Alvo formato *alvo_f_0x*.

Passos
-------
#. Rodar na pasta de calibrações

    .. code:: bash

        epar calib_spec

    Para economizar tempo, é possível copiar a solução das linhas da lâmpada de calibração. Porém **é necessário comparar a posição da fenda 1** para escolher o arquivo adequado.

#. Rodar na pasta do alvo

    .. code:: bash

        epar calib_spec

#. Caso não esteja satisfeito com a solução do contínuo, rode o comando abaixo, a ser aplicado em todos os arquivos `\*.ms.cal.fits`.

    .. code:: bash

        extract_ms_iraf.py


MUSICOS com OPERA
===================
Todos os arquivos na pasta da noite. A separação entre imagens de calibração e objetos é feita pelo *header*. O nomes padrão para são *bias\**, *flat\*, *lamp\**, e o restante é considerado alvo. 

Passos
-------
#. Verifique se o cabeçalho das imagens estão corretos com o comando 

    .. code:: bash

        operaQueryImageInfo -r ./ -e "INSTMODE OBSTYPE OBJECT EXPTIME2 DATE MODDATA"

**Opcional**: Rodar `prepare_header_opera.py` na pasta da noite. Rode com a opção `-h` para a acessar a ajuda. Note que a rotina assume o mesmo modo (*RED* ou *BLUE*) para todas modificações no *header* (bias e flat deveriam ser indiferentes ao modo). Assim, se há dois modo na noite, especifique explicitamente o formato dos nome. Exemplo: 

    .. code:: bash

        prepare_header_opera.py -B -l "lamp_b*" -o "*_b_*"

#. Rodar o processamento das calibrações da noite

    .. code:: bash

        mkdir reduc
        operaMusicos.py --datarootdir=../ --pipelinehomedir=$HOME/opera-1.0 --productrootdir=./reduc --night=./ --product="CALIB" -pvts
        # "-s" means SIMULATION of the reduction...

#. Rodar o processamento dos alvos da noite

    .. code:: bash

        operaMusicos.py --datarootdir=/data/MUSICOS/ --pipelinehomedir=$HOME/opera-1.0 --productrootdir=$HOME/Reductions/MUSICOS/ --night=14set05_R --product="OPSPC" -pvt

#. Caso não esteja satisfeito com a solução do contínuo, rode o comando abaixo, a ser aplicado em todos os arquivos `\*.spc.gz`.

    .. code:: bash

        extract_ms_opera.py


Sobre as rotinas `extract_ms_\*`
----------------------------------
Basicamente faço o seguinte: leio os espectros e pego o lambda e o fluxo não normalizados. Há um algoritmo que ajusta o contínuo baseado nos maiores valores a cada espaçamento regular de dados; neste ajuste, os pontos onde a variação é muito grande (o critério exato é onde a derivada do contínuo é maior que a mediana das derivadas) são excluídos. Ajustando isso a cada ordem, eu as linearizo em lambda de acordo com a maior resolução presente (interpolação linear no fluxo) e faço uma soma e divisão nas zonas de sobreposição. Por fim, resta uma variação de alta frequência no contínuo que eu filtro com o algoritmo de Savitzky-Golay em caixa pequena.


Resultados
------------
.. code:: bash

    $HOME/opera-1.0/pipeline/pySpectralAnalysis/plotSpectrum.py —spectrumfile=HR8634_R_001.spc.gz
    
    gunzip -c HR8634_R_002.spc.gz > HR8634_R_002.spc
    gnuplot -persist ../14set05Plots/HR8634_RED.gnu
    gnuplot -persist ../14set05Plots/HR8634_RED_norm.gnu

Problemas
-----------
- Não encontra *object*. Solução: verificar *header*.

Motivação
************
Michel Serres, Roda Viva:

    A palavra "anjo" (...) vem do grego angelos, que significa mensageiro, aquele que leva a mensagem. (...) antes de escrever o livro, que não tínhamos nenhuma teoria filosófica referente à sociedade de informação. E, como todos temos profissões de transportadores e interceptadores de mensagens, pensei "mas, afinal, quando na Idade Média os filósofos inventaram a teoria dos anjos, isto é, a angelologia, o que tinham em mente?" Eles tinham em mente, meu senhor, a utopia da sociedade da informação. Eles tinham tido a idéia de que se podia imaginar operadores encarregados justamente de tarefas que só a tecnologia de hoje permitiu realizar. (...) Por exemplo, dizem sempre que os anjos são invisíveis. É verdade, vocês nunca os viram, eu também não. Mas por que são invisíveis? Eu vou dizer. Estou falando em francês, mas os telespectadores estão ouvindo a mensagem em português. Há, portanto, entre mim, o emissor da mensagem, e o telespectador, o receptor da mensagem, alguém que trata a mensagem. Onde ele está? Ele não está aqui. O telespectador não o vê. Eu não o vejo. Vocês também não, mas, sem ele, nada seria possível, já que falo em francês e vocês ouvem em português. Conseqüentemente, é um anjo. E **quanto melhor ele faz seu trabalho, menos ele aparece**. O tradutor está ausente. Aliás, agradeçamos a ele por estar ausente; ele não apareceu ainda. Suponhamos agora que, em vez de traduzir fielmente a minha mensagem, ele diga o contrário. Vamos ficar preocupados. Vamos ficar bravos. Isso pode causar, entre nós, discussões que não teriam acontecido, talvez afrontas, talvez até guerras. Neste momento, ele existe. Ele afirmou sua presença. Eu o vejo. E, quando o vejo, significa que é um anjo mau. Entendem? 


Contato
*************
- Este tutorial: "Daniel Moser" <dmfaes \@ gmail.com>
- Pipeline MUSICOS no OPERA: "Eder Martioli" <emartioli \@ lna.br>


Referencias
*************
OPERA - Open source Pipeline for ESPaDOnS Reduction and Analysis
    http://cfht.hawaii.edu/en/projects/opera/

OPD/LNA - Instrumentos e Detectores
    http://www.lna.br/opd/instrum/instr.html

Dicas Python
    `Python and Astronomy <python_astro.html>`_