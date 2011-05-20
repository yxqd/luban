import numpy

from Functor import Functor


from Sin import Sin
from Exponential import Exponential
functor_types = [Sin, Exponential]


from dsaw.model.Inventory import Inventory as InvBase
class CurveComputation(object):

    function = None
    xmin = 0.0
    xmax = 10
    xstep = 0.1

    class Inventory(InvBase):
        
        function = InvBase.d.reference(
            name='function',
            targettype=None, targettypes=functor_types,
            owned = 1)

        xmin = InvBase.d.float(name='xmin', default=0.)
        xmax = InvBase.d.float(name='xmax', default=10.)
        xstep = InvBase.d.float(name='xstep', default=0.1)


    def __call__(self):
        xmin = self.xmin
        xmax = self.xmax
        xstep = self.xstep
        x = numpy.arange(xmin, xmax, xstep)
        f = self.function
        return x, f(x)
