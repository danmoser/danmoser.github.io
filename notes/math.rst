Math
#########

.. contents:: Table of contents

Relations
===========
:math:`\frac{1}{a}\pm\frac{1}{b}=\frac{b\pm a}{ab}`

Approximations
=================
:math:`A\exp(-\tau) \approx (1-\tau)A`, if :math:`\tau\ll 1`.

:math:`f(x)\simeq f(x_0)+\frac{f'(x_0)}{1!}(x-x_0)+...+\frac{f^{n}(x_0)}{n!}(x-x0)^n`

Paraxial angles
-----------------
:math:`\tan\theta\approx\theta`

:math:`\sin\theta\approx\theta`

:math:`\cos\theta\approx 1-\frac{\theta^2}{ 2}\approx1`

Trigonometric relations
------------------------
:math:`\sin\alpha+\sin\beta=2\sin\left(\frac{\alpha+\beta}{2}\right)\cos\left(\frac{\alpha-\beta}{2}\right)=2\sin\frac{\alpha}{2}\cos\frac{\alpha}{2}+2\sin\frac{\beta}{2}\cos\frac{\beta}{2}`

:math:`\sin\alpha+\sin\beta=2\left(\cos^2\frac{\beta}{2}+\sin^2\frac{\beta}{2}\right)\times\left(\sin\frac{\alpha}{2}\cos\frac{\alpha}{2}\right)+2\left(\cos^2\frac{\alpha}{2}+\sin^2\frac{\alpha}{2}\right)\times\left(\sin\frac{\beta}{2}\cos\frac{\beta}{2}\right)` 


Ellipse
=======
:math:`\frac{x^2}{a^2}+\frac{y^2}{b^2}=1`, where :math:`a>b` and the focus on :math:`x` axis. 

:math:`x = a\cos\theta` and :math:`y = b\sin\theta`.

The focus are :math:`\pm c = \pm a \times e`, where the eccentricity is :math:`e = \sqrt{1-\frac{b^2}{a^2}}`.

Parametric ellipse
---------------------
Or Trammel of Archimedes is the definition of :math:`a \equiv p+q` and :math:`b = q`.

If :math:`q\equiv 1`, then :math:`p=\sqrt{1-e^2}-1`.  


Rotation matrix (Euler angles :math:`\alpha, \beta, \gamma`)
===============================================================
.. math::

    R_x = \left[ \begin{array}{ccc}
    1 & 0          & 0           \\
    0 & \cos\alpha & -\sin\alpha \\
    0 & \sin\alpha &  \cos\alpha \end{array} \right]

    R_y = \left[ \begin{array}{ccc}
     \cos\beta & 0          &  \sin\beta  \\
    0          & 1          &  0          \\
    -\sin\beta & 0          &  \cos\beta  \end{array} \right]

    R_z = \left[ \begin{array}{ccc}
     \cos\gamma & -\sin\gamma &  0          \\
     \sin\gamma &  \cos\gamma &  0          \\
     0          &  0          &  1          \end{array} \right]

    R = R_x \cdot R_y \cdot R_z

In python:

.. code :: python

    R = np.dot(Rz,(np.dot(R_x,R_y)))


Gaussian
============
:math:`f(x)=a e^{-\frac{(x-b)^2}{2c^2}}+d`

:math:`\int_{-\infty}^\infty f(x)\,dx=ac\sqrt{2\pi}`, since :math:`\int_{-\infty}^\infty e^{-x^2}dx = \sqrt{\pi}`.

The scale height :math:`H` is :math:`P=P_0e^{-h/H}`.

English
==========
`Math expressions in English (PDF) <../static/math_English.pdf>`_

