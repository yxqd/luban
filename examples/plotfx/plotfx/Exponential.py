import numpy

from Functor import Functor
class Exponential(Functor):

    c = 1.0
  
    def __call__(self, x):
        c = self.c
        return numpy.exp(c*x)
