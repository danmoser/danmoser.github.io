Astrophysics Topics
#########################

.. contents:: Table of contents

Absolute flux units and magnitudes
************************************
...

Meetings
*********
http://www1.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/en/meetings/

Variable stars
****************
Variable star are defined as "stars having an apparent property changing with time" (usually their brightness). These properties can be:
- intrinsic: stellar luminosity actually changes (e.g., pulsations);
- extrinsic: owing to changes in the amount of light reaching Earth (e.g., eclipses).

*All* stars have some variation in luminosity. The Sun's luminosity varies about 0.1% over a *solar cycle*.

The first historical variable star is the Algol system, known nowadays to be a eclipsing binary system. Its variability was record in the old Egypt. In the modern times, it was notes the variability of the Mira star (Omicron Ceti) in 1638.

The famous *General Catalogue of Variable Stars* was the first list of variable stars created by the Academy of Sciences of the USSR, and continuously been updated by Russian researchers. In 2008, 46000 variable stars were known in the Milky Way, 10000 in other galaxies and a list of 10000 candidates exist.

The variabilities are classified as photometric or spectroscopic. They can be Periodical, Semiperiodical, Irregular or Unique. Examples: changes in velocities (spec. shifts) are a signal of binary system; abnormal emission or absorption lines indicate circumstellar activity and/or magnetic field...

Nomenclature
=============
In a given constellation, the first variable star discovered were designates with the letter *R* (and continuously until *Z*). Then, *RR*...*RZ*, *SS*...*ZZ*. Then *AA*...*AZ*, *BB*...*QZ*, with J omitted. After exhausted the total of 334 possibilities, stars as *V335*, *V...*.

The subgroups of variabilities are divided according to their *prototype*.

Intrinsic variabilities
-------------------------
- Pulsation, Eruption, Cataclysmic/Explosive...

Pulsation
^^^^^^^^^^^^
- Radial or non-radial
- Fundamental frequency (:math:`f_0`) determining the period.
    - Harmonic or overtone (:math:`n>1`)
- It the variability has a complex shape (no clear frequencies), it is called irregular or stochastic. 

The modes of pulsations can be:

- p-mode = pressure (or acoustic) mode, driven by internal pressure fluctuations within a star; their dynamics being determined by the local speed of sound. Shape: reflections at stellar surface.
- g-mode = gravity mode, driven by buoyancy (aka restoring force). Shape: elliptical movements around the stellar core.
- f-mode = surface gravity modes. Shape: akin to ocean waves along the stellar surface.


Extrinsic variabilities
-------------------------
- Eclipsing, multiple stars (rv)
- Rotating variables ("spots")

Shape missions
=================
- MOST 
- CoRoT
- WIRE
- SOHO (exclusive to the Sun)
- Kepler
- BRITE (a constellation of six nanosatellites. Sizes: cube os 20 cm!)

Peculiar stars
====================
Excellent reference is http://www.astrosurf.com/buil/us/peculiar.htm, were there are lists of bright Bp/Ap and Herbig Be/Ae stars.


Astrophysical disks
*********************
http://www.damtp.cam.ac.uk/user/hl278/DAD.html


Observational
*****************
=== === === ===
mes RA0 RAm RAf
=== === === ===
Jan 00  08  16
Fev 02  10  18
Mar 04  12  20
Abr 06  14  22
Mai 08  16  00
Jun 10  18  02
Jul 12  20  04
Ago 14  18  06
Set 16  00  08
Out 18  02  10
Nov 20  04  12
Dez 22  06  14
=== === === ===

ESO Periods
=============
- Period Odd  - 01 Apr to 30 Sep (RA limits: ~10h to ~02h)

    *deadline* ~ 01 Oct

- Period Even - 01 Oct to 31 Mar (RA limits: ~22h to ~14h)

    *deadline* ~ 01 Apr

OPD Periods
==============
- Período Verão - 01 set a 28* fev (RA limits ~20h a ~12h)

    *Limite* ~ 30 abr

- Período Inverno - 01 mar a 31 ago (RA limits: ~08h a ~00h)

    *Limite* ~ 31 oct

Spectro-astrometry
*********************
The spectro-astrometric technique is a method for studying the spatial structure of astronomical sources on scales well below the normal limit on resolution set by the seeing disk size or the diffraction limit. It relies on the fact that the relative position of a source at two or more wavelengths can be measured to an accuracy limited only be photon statistics, if the measurements are simultaneous. 

The technique is being used for the study of structure in pre-main-sequence stars, where it can be used to detect binary companions and to study the outflows from the stars. It is also being used to study the structure of the narrow line region in active galactic nuclei. 


About fluxes and conversions
*******************************
The relation of Black Body curves are:

.. math::
    
    I(\lambda, T)d\lambda = I(\nu, T)d\nu

And convertion of units:

:: 

    [Y erg/cm^2/s/Hz]dHz = [X1 erg/cm^2/s/A]dA
    dHz/dA = "(c/A)'dA" = -c/(A)^2
    [Y erg/cm^2/s/Hz] = dA/dHz * [X1 erg/cm^2/s/A]
    [Y erg/cm^2/s/Hz] = (1/c) * [X2 A]^2 * [X1 erg/cm^2/s/A]
    # c = 3e18 A/s
    [Y erg/cm^2/s/Hz] = 3.335641e19 * [X2 A]^2 * [X1 erg/cm^2/s/A]

:: 

    # Hdust models: (ergs/s/cm2/mu) * 1e-4 = (ergs/s/cm2/A) 
    


Interferometers
****************************
ESO interferometers
====================
- VINCI: First VLTI generation. ? BAND, 2 telescopes, ? resolution
- MIDI: Second VLTI generation. ? BAND, 2 telescopes, ? resolution
- AMBER: JHK bands, 3 telescopes. R=(30?, 1500 and 12000) resolution modes. PROBLEMS with absolute visibilities calibration. 
- PIONIER: H band. 4 telescopes. 3, 9 channels (resolution)
- MATISSE: ?
- GRAVITY: ?


CHARA interferometers
======================
- ALOHA: H band. 4? telescopes. R=1250-9300? (resolution)
- MIRC: H band?
- VEGA: ?

Other interferometers
=======================
- NPOI: Kenneth J. Johnston, Navy Precision Optical Interferometer. V band (Halpha).?


Organize
**********
http://www.aps.org/publications/apsnews/201501/stories.cfm

http://www.osti.gov/accomplishments/smoot.html

http://news.ucsc.edu/2014/10/exoplanet-atmosphere.html

http://www.nobelprize.org/nobel_prizes/physics/laureates/

http://www.space.com/19425-astronomy-prizes-scientists-awards.html

http://www.aps.org/publications/apsnews/201402/newsmakers.cfm

Links
======
Astronomical Imaging using Polarizing Filters and Stokes Parameter Imaging Technique
    http://narrowbandimaging.com


Statistics
**************
http://astronomy.swin.edu.au/~cblake/stats.html

VO
********
ESA Sky: 
- http://arxiv.org/abs/1512.00842
- http://archives.esac.esa.int/esasky-beta/