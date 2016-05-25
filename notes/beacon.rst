BeACoN Meettings
#######################

.. contents:: Table of contents

Links
*********
- Missões LNA
    http://bit.ly/1ZQyzaJ
    
- Distribuição de tempo
    http://www.lna.br/distempo/divtempo.html
    
- Formulários (usuários OPD)
    http://www.lna.br/opd/info_obs/info_obs.html

- `Spartans movie <movs/beacon_spartans.zip>`_


Meetings
*************

2015-10-28 [Moser@OPD]
========================

2015-10-21 Xuxu + Leandro
======================================
Xuxu - Pseudo-photospheric models
------------------------------------
Or disk brightness profile.

:math:`\tau_z \geq 1` (vertical optical depth) sets the transition between thin and thick optical regime for each :math:`\lambda`.

Effective radius :math:`\bar{R}(\lambda, n_0, i)` is defined at :math:`\tau\sim1` at midplane. This is paper I.

For paper II, Rodrigo is proposing fitting AKARI, WISE and X infrared measurements in and statistical analysis.


Leandro - Fitting Be stars lightcurves
---------------------------------------
MACHO survey has a spectroscopic correspondent.

OGLE does not have. But they are likely Be stars, strong candidates. *B* and *I* filters observed.

Diffusion equation depends on :math:`M, T, \alpha`

Assuming to exponential components: a growing one and another for dissipation.

The fitting is done in a grid of *singleBe* models. 


2015-10-14 [No meeting = Python Boot Camp]
=============================================

2015-10-07 Alex (Sobolev) + Rivi
======================================

2015-09-30 [No meeting = SAB]
======================================

2015-09-23 [No meeting = Alex Russia]
======================================

2015-09-16 [No meeting = Alex Russia]
======================================

2015-09-09 Moser teaser
========================================
True defense preview.

2015-09-02 Short talks/Moser teaser
========================================
Alex left earlier...

2015-08-26 Short talks/André
========================================
Present: Marcelo, Mohammad, Dai, Leandro, Rodrigo, Fellipy, André, Moser

Robert and radio
------------------
Robert continued a project to observe stars on radio. The observations (~5 stars) show that disks extends up to 200 :math:`200R_{eq}`. Fitting the SED, from visible to radio wavelengths, shows a systematic slope of :math:`n\approx3.1-3.2\neq3.5` from the steady-state solution, a pure Hydrogen disk. 

This is likely the result of disk temperature decreasing with radius. MAYBE hydrodynamic considerations yield to lower disk temperature to a slope of 3.0.

Other explanation is the present of Helium as a disk coolant. The presence of Helium in the radiative transfer would change the disk from a isothermal structure to a decreasing temperatures yielding 3.0. This was suggested by earlier studies (~1970's) on stellar WINDS that could be applicable to Be disks.

Dai and the B[e]
-----------------
Dai is fitting and B[e] star (RS ??) in one of the Magellanic Clouds. The distance is 49.97+/-1.11 kpc (Pietzyński, ??). For Dai master, the :math:`\dot{M}` value used for fitting was :math:`1-10\times10^{-6}M_\odot`/yr/sr. She showed the results for :math:`5\times10^{-5}M_\odot`/yr/sr, and the results appeared to *do not converge*...

Alex suggested Dai to present in a future meeting the thesis of Will Robson. One of the main results of his thesis is that, the absence of 9.7 microns feature in some proto-planetary disks can be explained by the creation of a ice mantel around small grains in the disk. This conclusion was based on high-energy particle collisions with dust particles, and offers an alternative explanation to the absence of the feature due to an average bigger size of the disk grains (not likely). 

André and the Polarization as a diagnostic tool
-------------------------------------------------
Summary of Bjorkman & Bjorkman, 1994, (BJ94) on spectropolarimetry around the Balmer jump (BJ; UV observations).
The lower level of polarization *before* the jump could be explained by the central-star high-rotation. This was compared to the polarized SED of the star Zeta Tau.

A positive slope in the polarized spectrum in visible was not expected and was discovered by Klement et al., 2015. 

André showed images and surface brightness curves of the unpolarized and polarized regions of the Be disks. Conclusion is that polarization is coming from regions very close to the stellar surface. 

The conclusion of the positive slope only occurs for low-density disks :math:`(\Sigma_0<0.1` g/cm2) and stars with high-rotation :math:`(R_{eq}/R_p\gtrsim1.4)`.

A new window will be open by the *Spektr-RG* (SXG or SRG) satellite (https://en.wikipedia.org/wiki/Spektr-RG), having a spectropolarimeter at UV wavelengths. Other UV satellites are *Astrosat* (https://en.wikipedia.org/wiki/Astrosat) and *Spektr-UV* (https://en.wikipedia.org/wiki/Spektr-UV; but it appears to be just another name of the SRG).

**Question to understood**: Why the depolarization is stronger in the UV (i.e., before the BJ) than in the visible (after BJ)? Answer in BJ94.

According to Brown & McLean 1977, the polarization of Be disks can be understood as function of a *shape* factor (:math:`\gamma`) and :math:`\bar{\tau}`, the mean scattering optical depth. According to Alex, the rotation necessarily would **decrease** the mean scattering optical depth.

Alex did not agreed with the models André showed with a **increasing** polarization with rotation in the *BeAtlas*. Rodrigo emphasized that the goal was not the **level**, but the **slope**. He answered saying that the slope **was** a function of the level, so the directed comparison between models was not accurate.

**Something that wasn't discussed in the meeting**: the polarization in the *BeAtlas* models **decrease** with rotation, as "expected", if a inclination angle o :math:`i\lesssim60` deg is considered (at least for low-density disks). Rodrigo told me that me models shown were for :math:`i\sim70` deg, were the maximum of polarization occurs. IMHO, for :math:`i>60` deg effects of self absorption become important so that the polarization can **increase**. 

I took a quick look in BJ94, and they predicted I quite strong polarization decrease for :math:`i=60` deg. On the other hand, they used a quite different model for the star :math:`(\beta=0.25`) and a strange density distribution for the envelope:

.. math::

    n_e=n_0\frac{[1+B\sin^m\theta]}{r^2[1-0.96R(\theta)/r]^b}.
    
It appears that, while André is exploring the diagnostic potential of the phenomenon, Alex wants to explore the theoretical foundations of it. IMHO, it should be assessed be possibility of "redo" BJ94 with more precise envelope models and Rodrigo's opacity description...


2015-07-01 to 2015-08-19 [No meetings]
========================================
Vacations + Moser's thesis.


2015-06-24 Moser + Vieira
===========================
- Alex's mug!
- Moser, new results for Achernar!

Rodrigo's Papers (I and II)
----------------------------
Rodrigo develop an analytic model to the emission of Be systems: star + optical thick + optical thin disk components. It is possible to predict 2D brightness distributions to (roughly) any inclination angle not edge-on (equator-on).

The model works good for mid/distant-IR, because of gauss factors.

Rodrigo took archive IR data (IRAS, AKARI, etc) and compared the best fit using Frémat 2004 atmospheric modeling (2MASS, due to short wavelengths, is not good to model). He fitted :math:`n_0` and :math:`m`, the volumetric density exponent, to infer the :math:`\dot{M}`. His :math:`\dot{M}` determinations are 2 order of magnitudes lower than the ones predicted by Waters 1987. This agrees with Anahi's work on late 2014.

He found:

- 3 peaks in :math:`n_0` distribution: hotter stars tends to create denser disks (Teff>18000; 15000<Teff<18000; Teff<15000)!
- NO DEPENDENCE of Teff with :math:`m`: MYTH of late-B types have more stable disks busted!
- It is possible to do :math:`m`-age relations. Ages of disks, and metallicity correlations.
- No :math:`m<3.5` and high :math:`n_0`: limits on correlations.


2015-06-17 [No meeting]
=========================


2015-06-10 Bednarski Polarimetric reduction
============================================
Bednarski: Polarimetric reduction
------------------------------------------------------
Reduction with IRAF
^^^^^^^^^^^^^^^^^^^^^^^^^^
- `Calib`
- `Reduce`

Goal: generate ``*.out`` files.

Generating night's tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- `GenAllLog`: generate ``std.log`` and ``obj.log`` files for a night.
    Search ``*.out`` files in subdirectories.

Extracting the temporal series
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- `genTarget`: generate the times series, looking for ``*.log`` files.


Discussion with Leandro, Rodrigo and Alex
------------------------------------------------------
.. math:: \tau=\frac{1}{\cos i}\Sigma(R,t)\kappa(R)

*SPH* connected with Xuxu's models (Despina+Rodrigo). Leandro is working on *SingleBe* and Xuxu's models.

2015-06-03 Bruno + Daniel Moser short talks
============================================
Bruno's talk: *emcee* and *UV* bump at :math:`2200\AA`
-------------------------------------------------------
*emcee*: better results fixing one parameter (e.g., oblateness). Otherwise, parameters are kind of undetermined.

*UV* bump (2200 :math:`\AA`) = 4.54 :math:`\mu m^{-1}`. Whole bump between 3 to 6 :math:`\mu m^{-1}`.

3 kinds of extinction? = bump strength can change depending on something(?) and on the kind of grains present. This is also related with :math:`R_V`.


Moser's talk: Aeri
------------------^
No further details (see log, perhaps).


2015-05-26 [No meeting]
======================================

2015-05-20 Rubinhos's Master preview
======================================
- 45 to 50 minutes
- In Portuguese

"A Estrutura do Campo Magnético do Meio Interestelar a partir de Observações de Aglomerados Abertos".

Intro:

- MI
- Aglomerados Abertos
- Polarização

Metodologia:

- Observações
- Parâmetros de Stokes
- Redução de Dados

    :math:`P/\sigma_P>5`

Análise:

- 5 campos

Conclusões:

- ...


Perguntas:

- Por que aglom. aberto?

    Distância e comp. química similares
    Grande número de estrelas

- WEBDA?
- Primeira média? Média total.
- Estrelas com números? 
- Q, U = 8% ? Sim!! 
- Incertezas B pequenas...
- Box diagrama Q, U?
- Para quê o DHR? Só SP são analisadas?
- Origem campos uniformes vs. campo turbulento
- Magnitude 18 no OPD? Redutor focal?

Sugestões:

- `et al`, `box`
- < 10%, > 90%
- Fotos na sala de defesa
- Destacar transições


2015-05-13 Daiane's Master preview
======================================
- 45 to 50 minutes
- In Portuguese

"Envelopes de Estrelas Supergigantes B[e] nas Nuvens de Magalhães".

5 estrelas observadas em espectropolarimetria. 1 modelada (*hdust*).

Introdução:

- Contexto: próximas às LBVs e WRs. B[e]'s:

    - Intensas linhas Balmer
    - Intenas linhas FeII, proibidas
    - Excesso infravermelho

- Polarimetria
- Ventos
- *hdust*

Observações:

- Dados brutos e redução
- Explicativa e dados finais

Modelos:

- [Dúvida] de onde vieram os parâmetros? Componentes?

Conclusões:

- [Dúvida] Polarização meio-interestelar

Pode ser tirado:

- excesso WR, LBV, sgB[e]
- HPOL
- (mecanismos de polarização)

Geral:

- [Correção] Mudança de escala na apresentação de dados.
- [Correção] Q U com barras de erros
- [Correção] Explicação discrepâncias Q U
- [Dúvida] Distância temporal dos dados


2015-05-07 Group's results
============================
A few notes since my laptop was in use to projection.

- Moser's talk about Achernar's :math:`H\alpha` line profiles
    - Equivalent Width, Peak separation
- Mohammad's talk about the four lightcurve cycles of 28 CMa
    - Reservoir effect: 2012 article of Alex is "wrong" 

2015-04-29 Cyril 
============================
How to run Atsuo's code (3D!).

Math in appendix of Cyril's paper. Basically are conservative equations (mass, momemtum) with classic perturbation (:math:`e^{wt-\phi}`).

The parameters are stellar ones (:math:`R_*,R_{env}`,etc) + frequency space where perturbations can be propagated (*eigenfrequencies*).

There are 3 routines:

- onearm3D
- ef3D
- table2.5D

First compile, then run as ``./run_ROUTINE < input_file``.

2015-04-22 [Alex in Canada]
==============================

2015-04-15 [Alex in Canada]
==============================

2015-04-08 Group's results
============================
A few notes since my laptop was in use to projection.

- Cyril and interferometric fitting. Absorption issue.
- Rodrigo and his first paper (new :math:`\dot{M}`).
- Bednarski and field stars.


2015-04-01 [Holy Week]
========================

2015-03-25 Robert
==================
Beta CMi - choose a stable (an isolated) Be star to explore the disk, mainly the outer part. Archive data to radio.
Radio observations to constraint its size.

Be stars are not good targets to ALMA: small angular size.

Start modeling with the central star: 5 pars = M, Tp, W, Beta* and L (Z is important to Mag. Clouds).
High rotation rate. Interferometry import to constraint parameters ranges.

IUE spectrum import to constraint the central star = consensus: B8 and i~35deg.
Influence of the disk starts at ~2500Angs.

    - André's project to BeAtlas: influence of the disk in the IUE spectrum. 

* Fixed rotation and inclination = M has no influence in the same spectral range.
* Constrained L and polar radius.

Halpha, Hbeta, Hgamma and Bracket gamma.
It is tricky to fit simultaneously Halpha and Hbeta!!

There are small V/R variations: due to a binary companion. 180 days period.

HPOL measurements.

Visible and nearIR are sensible to density of the disk !!!

Models:

* parametric = rho_0, n, H0(Tk), Rout
* mixed = rho_0, n, Rout
* self-consistent = Mdot/alpha, R_0, Rout

Robert is measuring Rbar and no Rout.

n is not 3.5. It is 3.0. Impossible to fit 3.5 changing Rout.

3.5 is good til 10 microns. 3.0 is good beyond that.

n=3.5 wrong BrGamma interferometry.

Best detailed model of a Be star so far.

Zeta Tau could be done same analysis if there is no global density waves in the disk.

- HPOL level = crap

Best inclination determination comes from AMBER data. 


2015-03-18 Despo
=================
Smoothed-particle hydrodynamics
http://en.wikipedia.org/wiki/Smoothed-particle_hydrodynamics

SPH is not a grid code... It 'probes' the dynamics if variable mass particles.

SPH computational timescale :math:`n*\log(n)`; `n` = no. of particles

Binarity: changes the surface density profile: dissipates the outer disk. The inner disk is approx. unchanged. How much mass is transfered to the secondary can be estimated.

Be-Xray binaries: compact object (Black Hole! or neutron star). Material is accreted in the companion (Be-GammaRay).

"Watershed" effect: change of the slope in dens. prof. at outer radius due the companion.

.. math::

    \Sigma = A\frac{(r/R_t)^{-m}}{1+(r/R_t)^n} 

    \Sigma = \frac{\dot{M}}{\alpha}\ldots

.. Teste :math:`\pi`. E teste continua.

For high eccentric orbit the truncation radius *grows*, because of the way disk interacts with the companion...

Euler angles... define misalignment and unambiguously define rotation!
Pleione is a famous case of misalignment (equatorial plane of the Be star and the companion orbit plane).

This process could explain the transition seen in some Be stars from shell spectrum to normal Be case! Warped disks!

Another problem: prograde/retrograde motion between the Be star rotation and the companion.

    - Mass injection rate = Mass disk injection (some material returns to the star)
    - Mass decretion rate
    - Mass-loss rate


Other
*********
Spartans
============
- `Subtitles <movs/spartans.srt>`_
- `Movie <movs/spartans.mp4>`_
