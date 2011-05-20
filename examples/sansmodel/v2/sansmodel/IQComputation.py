

from SphereModel import SphereModel
from CylinderModel import CylinderModel
modeltypes = [SphereModel, CylinderModel]


from dsaw.model.Inventory import Inventory as InvBase
class IQComputation(object):

    model = None

    Qmin = 0.0
    Qmax = 1.0
    Qstep = 0.02


    class Inventory(InvBase):
        
        model = InvBase.d.reference(
            name='model', targettype=None, targettypes=modeltypes, owned=1)

        Qmin = InvBase.d.float(name='Qmin', validator=InvBase.v.nonnegative, default=0.)
        Qmax = InvBase.d.float(name='Qmax', validator=InvBase.v.nonnegative, default=1.)
        Qstep = InvBase.d.float(name='Qstep', validator=InvBase.v.positive, default=0.02)


    
    def customizeLubanObjectDrawer(self, drawer):
        drawer.sequence = ['model', 'properties']
        return
    
