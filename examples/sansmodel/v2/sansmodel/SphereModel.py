from dsaw.model.Inventory import Inventory as IBase
class Inventory(IBase):
    radius = IBase.d.float(name='radius', validator=IBase.v.positive, default=10.)
    radius.tip = 'unit: AA'
    scale = IBase.d.float(name='scale', validator=IBase.v.positive, default=1.)
    contrast = IBase.d.float(name='contrast', validator=IBase.v.nonnegative, default=1.e-6)
    background = IBase.d.float(name='background', validator=IBase.v.nonnegative, default=0.0)
    
    

def __establishInventory__(self, inventory):
    inventory.radius = self.getParam('radius')
    inventory.scale = self.getParam('scale')
    inventory.contrast = self.getParam('contrast')
    inventory.background = self.getParam('background')
def __restoreFromInventory__(self, inventory):
    self.setParam('radius', inventory.radius)
    self.setParam('scale', inventory.scale)
    self.setParam('contrast', inventory.contrast)
    self.setParam('background', inventory.background)


from sans.models.SphereModel import SphereModel
SphereModel.Inventory = Inventory
SphereModel.__establishInventory__ = __establishInventory__
SphereModel.__restoreFromInventory__ = __restoreFromInventory__


