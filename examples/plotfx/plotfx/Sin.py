import numpy

from Functor import Functor
class Sin(Functor):

    a = 1.0
    b = 0.0

    def __call__(self, x):
        a = self.a
        b = self.b
        return numpy.sin(a*x+b)
