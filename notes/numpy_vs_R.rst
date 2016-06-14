R compared to numpy
====================

=========================== =============================
R                           numpy
=========================== =============================
a <- c(33, 44, 92, 58)      a = np.array(33, 30, 92, 58)
a[a>30]                     a(np.where(a>30))
which.max(a)                np.where(a == np.max(a))
match(30, a)                np.where(a == 30)
*no not work*: match(30, a) *okay* np.where(30 == a)
summary(a)                  (not in numpy)

=========================== =============================

R: ``fx <- function(x) {x**2}``. Python: ``def fx(x): \n    return x**2``.

