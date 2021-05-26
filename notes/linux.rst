Linux tips
###############

.. contents:: Table of contents

Useful commands tricks
===========================
Command ``cmake`` and ``make``
--------------------------------
.. code:: bash

    rm CMakeCache.txt
    cmake ..
    make prefix=$HOME/.local/
    make DESTDIR=$HOME/.local/ install
    
Decrease Backlight Below Minimum
----------------------------------
.. code:: bash

    sudo nano /sys/class/backlight/intel_backlight/brightness
    # set the value to 1

How to mount an ISO file
---------------------------
.. code:: bash

    sudo mount /path/to/file.iso /path/to/mount -o loop #-t udf #-t iso9660
    sudo umount /path/to/mount 

How to create an ISO image
------------------------------
Creating an ISO from Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code:: bash

    mkisofs -o new.iso /path/to/folder

Ripping an ISO from a CD
~~~~~~~~~~~~~~~~~~~~~~~~
.. code:: bash

    dd if=/dev/cdrom of=/home/user/new.iso

Disable Web Notifications Firefox Browser
----------------------------------------------------
- Access "about:config"
- Search for "webnotifications"
- Disable (**false**) the (1) `dom.webnotifications.enabled` and (2) `dom.webnotifications.serviceworker.enabled`. 

One may also want to clean up the previous authorizations. For that, `Options > Content > Notifications > Choose... > Remove All Sites > Save Changes`.

Find a package by filenames
------------------------------
``apt-file``: https://wiki.ubuntu.com/AptFile . This is very useful when looking for Latex files, as `*.sty`.

Set size of files in multi-files zip
---------------------------------------
.. code:: bash

    7za a -m0=Copy -v512m output.7z input
    7za a -m0=lzma2 -mx0 output.7z input

    # -mx=[0|1|3|5|7|9]  5   Sets level of compression.
    # 0 = copy; 1 = fastest; 5 = default; 9 = max.

Print line interval
---------------------
Print from lines 4400 to 4500 of a file

.. code:: bash

    cat file | head -n 4500 | tail -n 100

Repair ``rar`` file
---------------------
.. code:: bash

    unrar x -kb damaged.rar

Good media player
--------------------
``mplayer`` (mplayer2) is the best!


Multiple files edition (substitution)
---------------------------------------
.. code:: bash

    sed -i "s/INPUT/OUTPUT/g" *.txt
    
Reminder: if you want to substitute a special character, write "\\" before it (e.g., "\\/").


Is there a way to echo an alias?
-----------------------------------
.. code:: bash

    alias ls
    # alias ls='ls --color=auto'


Disk usage
--------------
.. code:: bash

    du -h(s) folder

Returns the disk usage of ``folder`` recursively. "s" returns it *summed*.

Good program: ``baobab``.


``ls``
-------
.. code:: bash

    ls -ltr --time-style=long 
    ls -ltr --time-style=iso
    ls -ltr --time-style=full

Unix essential commands
-------------------------
:: 

    `awk`      tool for processing rows and columns.                       
    `bc`       calculate mathematical expressions.                                   
    `cat`      print the whole file on screen.                                       
    `cd`       change your current directory.                                        
    `chgrp`    change the group of the file.                                         
    `chmod`    change permissions of the file.                                       
    `chown`    change the owner of the file.                                         
    `cp`       copy a file.                                                          
    `cut`      select sections of text files (usually cols) by delimiters. 
    `date`     print the current date on screen.                             
    `diff`     shows in screen the differences between two files.              
    `du`       get information about disk usage and file sizes.              
    `echo`     print string on screen.                                             
    `expr`     calculate mathematical expressions.                                 
    `find`     find files in your computer.                                        
    `grep`     find string in file or list of files.                             
    `gzip`     compress/decompress files.                                          
    `head`     print first lines of a file.                                        
    `ifconfig` check network info (IP, mac address...).                        
    `ln`       create links (shortcuts) between files.                           
    `ls`       list files in directories.                                          
    `mkdir`    create a directory.                                                  
    `more`     print file on screen, pause in the way.                           
    `mv`       move files from directories and change their names.             
    `nohup`    leave process running in remote computer after you log off
    `passwd`   change your password.                                           
    `read`     get input from keyboard.                                            
    `rm`       remove (delete) a file.                                               
    `scp`      copy files to/from remote computers.                              
    `sed`      automatable, command-line text editing.                           
    `shred`    write zeroes on top of the file so it cannot be recovered.
    `sort`     sort lines in a text file.                                        
    `ssh`      connect to remote computers.                                        
    `tac`      print the whole file on screen, backwards.                        
    `tail`     print last lines of a file.                                         
    `tar`      put/extract files in a tarball.                                     
    `touch`    update 'last modified' date or create an empty file.          
    `wc`       counts words, lines and characters in a file.                   
    `wget`     download file from the internet.                                  
    `top`      find out which processes are running.                               
    `xargs`    pass input from pipeline as argument to a command.              

.. code:: bash

    # examples
    cat command_list.txt
    more command_list.txt
    head command_list.txt
    head -n3 command_list.txt
    head -n-20 command_list.txt
    tail command_list.txt
    tail -n3 command_list.txt
    tail -n-20 command_list.txt
    diff command_list.bkp command_list.txt
    wc command_list.txt
    wc -m command_list.txt
    wc -l *
    grep "example:" command_list.txt
    grep "List of examples" -A6 command_list.txt
    grep "List of examples" -A6 -m1 command_list.txt
    grep -nr "example:" command_list.txt
    grep -v "example:" command_list.txt
    grep "Other" command_list.*
    grep "Other" command_list.* -l
    grep "Other" command_list.* -c
    grep --help
    sort data/frutas.dat
    sort -n data/numeros.dat
    cut -d: -f1 command_list.txt
    cut -d/ -f3 data/listagem.dat
    awk '{print $2,$1}' data/listagem.dat
    sed -e "s/example/exemplo/g" -e "s/:/>/g" command_list.txt
    find ./ -name '*.dat'
    ln -s data/numeros.dat numbers.dat
    nohup <normal command> > output.txt &
    chmod 755 helloworld.sh

Symbolic link
-----------------
.. code:: bash
    
    ln -s {/path/to/file-name} {link-name}

Number of cores
-----------------
.. code:: bash

    nproc

``rm`` + ``find``
------------------
.. code:: bash

    find . -name "*~" -exec rm -r "{}" \;
    # or
    find . -name "*~" -print0 | xargs -0 rm
    # or for directories
    find . -name "svn" -type d -exec rmdir "{}" \;

``rsync``
-----------
.. code:: bash

    rsync -azP --delete --dry-run --rsh='ssh -p20001' Scripts/ user@machine:/paht/Scripts2
        # "/" = very important. Otherwise, without "/", it goes /paht/Scripts2/Scripts
        # -a = arquive (recursive)
        # -z = zip (for network)
        # --delete = to sync deletions
        # --dry-run = only show results 
        # -P = partially (resume)
        # --exclude X = ignora arquivos X, e.g. "*.pro"
        # --update = somente sobrescreve arquivos mais novos
        # --stats = estatistica da transferencia
    
    rsync -a -f '- /*/*/' /dirA/ host:/dirB/
        # -a triggers the archive mode that activates recursion 
        # -f is short for --filter=, which adds a file-filtering rule.
        #     The pattern is inside single quotes so that the shell does not expand
        #         wildcards; double quotes would work equally well in this case.
        #     - means this is an exclude pattern.
        #     The leading / means the pattern must start at dirA/ (the rsync "transfer-root").
        #     The */* part of the pattern refers to anything inside of a subdirectory.
        #     The trailing / limits the exclusion to directories.
        #     Files inside a subdirectory of dirA/ are not affected.

    # So in the end, rsync copies nothing more than one level down (and also does not
    # create second-level directories).


General Tips
================
Terminal
-----------
- *Ctrl+Shift+T* Open it
- *Ctrl+A* 	Go to the beginning of the line you are currently typing on
- *Ctrl+E* 	Go to the end of the line you are currently typing on
- *Ctrl+L* 	Clears the Screen, similar to the clear command
- *Ctrl+U* 	Clears the line before the cursor position. If you are at the end of the line, clears the entire line.
- *Ctrl+H* 	Same as backspace
- *Ctrl+R* 	Let’s you search through previously used commands
- *Ctrl+C* 	Kill whatever you are running
- *Ctrl+D* 	Exit the current shell
- *Ctrl+Z* 	Puts whatever you are running into a suspended background process. fg restores it.
- *Ctrl+W* 	Delete the word before the cursor
- *Ctrl+K* 	Clear the line after the cursor
- *Ctrl+T* 	Swap the last two characters before the cursor
- *Esc+T* 	Swap the last two words before the cursor

Also works on Mac OS.

Scripts
-----------
Script starts with ``#!/bin/bash``

Keeping windows opened
-------------------------
After opening then with ``program &``, just type ``disown``.


Useful keyboard shortcuts
---------------------------
.. code:: bash

    exaile -t  #Pause
    exaile -p  #Previous
    exaile -n  #Next
    qmmp -t  #Pause
    clementine -t  #Pause
    clementine -r  #Previous
    clementine -f  #Next
    amixer set Master 7%- -q
    amixer set Master 7%+ -q

Win programs alternatives
---------------------------
.. figure:: ../figs/linux_ref_progs.jpg
    :align: center
    :width: 640 px

Image tools
---------------
.. code:: bash

    sudo apt-get install imagemagick
    mogrify -quality 75 *

    # Para mudar a resolucao, onde nao havera nenhuma imagem com largura ou 
    #  altura maior do que 1280 pxs (O 'aspect ratio' eh sempre preservado):
    mogrify -resize '1280x1280>' *.jpg
    # Exemplos: 4608x3072 -> 1280x852
    # Exemplos: 3072x4608 -> 852x1280

    mogrify -resize '1920x1920>' -quality 75 *.jpg
    mogrify -resize '1920x1920>' -quality 75 *.JPG

    # fusao vertical
    convert -gravity Center -append input*.eps output.png 
    # fusao horizontal
    convert -gravity Center +append input*.eps output.png

    # Exemplo mais avancados
    montage rrm.pdf pol.pdf -geometry 800x800 output.pdf
    convert output.pdf -crop 1600x600+0+100 +repage out2.pdf

    convert teste.pdf -crop 100%+0+10% +repage out2.pdf

    montage vin.pdf xav.pdf -geometry 600x600 temp.pdf
    convert temp.pdf -crop 1200x460+0+70 +repage newfig1.pdf

Image to PDF format
----------------------
In principle, one could use ``convert`` for the job. However, it is annoying aligning and setting border. So, I suggest using ``img2pdf``.

.. code:: bash

    img2pdf input.png --pagesize 210mmx297mm --border 1cm:2.5cm -o out.pdf
    # --pagesize 210mmx297mm force the portrait mode. 
    # For landscape (or "auto"), use --pagesize A4.

Image to EPS format
----------------------
There are *several* recipes for doing this (e.g., ``convert img.png img.eps``).
By far, the best option is this:

.. code:: bash

    convert image.png image.pdf
    pdftops -eps image.pdf

You can also try (``eps3`` is a valid option):

.. code:: bash

    convert image.png eps2:image.eps

Attention! *BIMP* and *David's Batch Plugin* (gimp-plugin-registry) DO NOT WORK for EPS format...

(More about EPS-PDF convertion, formats and sizes, see `latex <latex.html>`_ page)


Cedilla
--------
Add the following to ``/etc/environment``:

.. code::

    GTK_IM_MODULE=cedilla 
    QT_IM_MODULE=cedilla 

GRUB edit
-----------
.. code:: bash

    sudo vim /etc/default/grub
    sudo update-grub


Changing time-zone
-------------------
Using the terminal (command line)

.. code:: bash

    sudo dpkg-reconfigure tzdata

Follow the directions in the terminal. The timezone info is saved in ``/etc/timezone``.


Problems with the panel
------------------------
On Xubuntu 16.04, if the indicator-multiload has problems ("transparency") or the volume indicator is missing, You might have indicator-plugin missing from the panel. 

Right click on the panel and select it.


Alternative to ``indicator-multiload``
-----------------------------------------
Install ``multiload-ng``!!!!

.. code:: bash

    sudo add-apt-repository ppa:nilarimogard/webupd8

    sudo apt update

    sudo apt install xfce4-multiload-ng-plugin

Then, (right click) Panel > Panel Preferences > (tab) Items > "+"


Mimes and program links in File Managers
------------------------------------------
In Ubuntu, the program-file type association is set is in ``~/.local/share/applications/mimeapps.list``.

Then, the program associated there must have a "description" in ``/usr/share/applications/PROGRAM.desktop``.

One example is here:

.. code:: 

    [Desktop Entry]
    Name=Foxit Reader
    Comment=View pdf documents
    Keywords=pdf;octet-stream;
    StartupNotify=true
    Terminal=false
    Type=Application
    #Icon=FoxitReader
    X-GNOME-DocPath=
    X-GNOME-Bugzilla-Bugzilla=GNOME
    X-GNOME-Bugzilla-Product=FoxitReader
    X-GNOME-Bugzilla-Component=BugBuddyBugs
    X-GNOME-Bugzilla-Version=3.14.1
    Categories=GNOME;Viewer;Graphics;2DGraphics;VectorGraphics;
    MimeType=application/pdf;application/octet-stream;
    Exec=/data/Softwares/Foxit/FoxitReader.sh
    Icon=/home/user/.local/share/icons/hicolor/64x64/apps/FoxitReader.png


Exporting wifi passwords
---------------------------
Network or wifi passwords are saved in ``/etc/NetworkManager/system-connections``. There is a file for each connection with its configuration and password. One need root privileges to read them (the files aren't encrypted).


Mounting a disk your user isn't the owner
--------------------------------------------
To mount a filesystem with special user id set, use ``bindfs``. 

.. code:: bash

    sudo apt-get install bindfs
    mkdir ~/myUIDdiskFoo
    sudo bindfs -u $(id -u) -g $(id -g) /media/diskFoo ~/myUIDdiskFoo
    # Keep the default mount running (do not eject)

More information: 
- http://www.penguintutor.com/linux/file-permissions-reference
- https://askubuntu.com/questions/34066/mounting-filesystem-with-special-user-id-set/353759#353759


Firefox + AdBlocl
-------------------
Open ``about:config`` in Firefox, and change the option at ``extensions.adblockplus.sidebar_key``!

Permitions
===========
.. code:: bash

    chmod a[ll],g[roup],u[ser] +/-x,r,w
    1 = execute
    2 = write
    4 = read
    7 = 1+2+4

To do it recursively:

.. code:: bash

    # To recursively give directories read&execute privileges:
    find /path/to/base/dir -type d -print0 | xargs -0 chmod -f 775 
    # To recursively give files read privileges: 
    find /path/to/base/dir -type f -print0 | xargs -0 chmod 664
    #
    # Other (not so efficient) ways are:
    find /path/to/base/dir -type d -exec chmod 755 {} +
    find /path/to/base/dir -type f -exec chmod 644 {} +
    # Or
    chmod 755 $(find /path/to/base/dir -type d)
    chmod 644 $(find /path/to/base/dir -type f)

How to apply default permissions
-----------------------------------
.. code:: bash

    chmod g+s <directory>  //set gid 
    setfacl -d -m g::rwx /<directory>  //set group to rwx default 
    setfacl -d -m o::rx /<directory>   //set other

Next we can verify:

.. code:: bash

    getfacl /<directory>

Output:

::

    # file: ../<directory>/
    # owner: <user>
    # group: media
    # flags: -s-
    user::rwx
    group::rwx
    other::r-x
    default:user::rwx
    default:group::rwx
    default:other::r-x

Users
----------
How can I add a new user as sudoer using the command line?

.. code:: bash

    sudo usermod -a -G sudo <username>

machine name
----------------
Error message when I run sudo: unable to resolve host(name)

- Edit ``/etc/hostname`` file contains just the name of the machine.
- Edit ``/etc/hosts`` accordingly.

SSH Auth
============
1- Run at local PC
---------------------
.. code:: bash

    $ ssh-keygen -t rsa
    #(3x type ENTER)
    #Your public key has been saved in <your_home_dir>/.ssh/id_rsa.pub
    $ scp ~/.ssh/id_rsa.pub USER@HOST:/sto/home/USER/id_rsa.pub
    #(Type your server's password)
    
2- Run at remote PC
------------------------
.. code:: bash

    $ cat id_rsa.pub >> ~/.ssh/authorized_keys
    $ chmod 700 ~/.ssh/authorized_keys
    $ rm id_rsa.pub
    
3- One may need to run at remote PC
------------------------------------------------
.. code:: bash

    $ exec ssh-agent bash
    $ ssh-add

GitHub
--------
.. code:: bash

    git config --global user.name "John Doe"
    git config --global user.email johndoe@example.com

https://help.github.com/articles/generating-ssh-keys/

.. code:: bash

    ssh-keygen -t rsa -b 4096 -C "user@gmail.com"
    # Enter file in which to save the key (/home/user/.ssh/id_rsa): /home/user/.ssh/id_github
    #
    # Type your github password...
    #
    # ...
    # The key fingerprint is:
    # 01:0f:f4:3b:ca:85:d6:17:a1:7d:f0:68:9d:f0:a2:db user@gmail.com
    
    cat /home/user/.ssh/id_github.pub
    # Copy and paste the PUBLIC key to https://github.com/settings/ssh

    # These steps may be required:
    # ..
    # start the ssh-agent in the background
    # eval "$(ssh-agent -s)"
    # Agent pid 59566
    #
    # If ~/.ssh/id_rsa do not exists:
    # ssh-keygen -t rsa
    #
    # Add your SSH key to the ssh-agent:
    # ssh-add ~/.ssh/id_rsa

Using PC MIC
===============
Tips
-------
Press "Record" and then check the "Recording" tab at the volume control.

Look for the "Monitor..." option.


How can I get the instrumentals only from a file and remove the vocals?
------------------------------------------------------------------------
A software that can do this is called ``sox``. It has an option for karaoke:

    *oops*

    Out Of Phase Stereo effect. Mixes stereo to twin-mono where each mono channel contains the difference between the left and right stereo channels. This is sometimes known as the ‘karaoke’ effect as it often has the effect of removing most or all of the vocals from a recording.

So from command line this ...

.. code::

    sox song.wav song_karaoke.wav oops

It must be in the WAV format.

To work directly on the MP3, you can also use ``audacity``.

    http://manual.audacityteam.org/o/man/tutorial_vocal_removal_and_isolation.html


No Sound with Headphones but Sound with Stereo
-------------------------------------------------
Sound card automaticly change to hdmi output when two applications conflicted with it. I fix that with the following command. It restore output to analog, again.

.. code:: bash

    alsactl -F restore


Listen to microphone over the speakers using pulseaudio
--------------------------------------------------------
By default, we cannot hear any sound of microphone over speaker on Debian or Ubuntu OS. So, we cannot sing karaoke. But this command can route the mic input through output:

.. code::

    pactl load-module module-loopback latency_msec=1

To turn it off:

.. code:: bash

    # Find the module NUMBER with
    pacmd list-modules
    # then to unload it:
    pactl unload-module 27

To add this permanently, you need to load the module when pulseaudio starts. To do this, you need to add a line to the ``/etc/pulse/default.pa`` (as sudo). The line can be added at the end of the file:

.. code::

    load-module module-loopback

**PROBLEM**: there is a lag in the mic audio using this method.


Listen to microphone over the speakers using Qjackctl
--------------------------------------------------------
.. code::

    sudo apt-get install qjackctl

Maybe you will need to add your user to the audio group (and restart the system).

To use it, "Start" and then "Connect".

 **PROBLEM**: No system audio - but no lag!


How to do a mixing
---------------------
Open you file in the Audacity.

Record your mic. The problem is: or you listen to yourself (and set out of sinc with the music, like with loopback) or listen only to the music.

I couldn't find a way record the voice while playing it in the right time (only with lag).


Summary
---------
QjackCtl: mic in the output, no lag. No system sound, and no record. 

Audacity + loopback: mic in the output, with lag. System sound, and record. 

Audacity: no mic in the output. System sound and record, no lag.

