from dsaw.model.Inventory import Inventory as IBase
class Inventory(IBase):
    radius = IBase.d.float(name='radius', validator=IBase.v.positive, default=20.)
    radius.tip = 'unit: AA'
    length = IBase.d.float(name='length', validator=IBase.v.positive, default=400.)
    length.tip = 'unit: AA'
    scale = IBase.d.float(name='scale', validator=IBase.v.positive, default=1.)
    contrast = IBase.d.float(name='contrast', validator=IBase.v.nonnegative, default=3.e-6)
    background = IBase.d.float(name='background', validator=IBase.v.nonnegative, default=0.0)
    
    

def __establishInventory__(self, inventory):
    inventory.radius = self.getParam('radius')
    inventory.length = self.getParam('length')
    inventory.scale = self.getParam('scale')
    inventory.contrast = self.getParam('contrast')
    inventory.background = self.getParam('background')
def __restoreFromInventory__(self, inventory):
    self.setParam('radius', inventory.radius)
    self.setParam('length', inventory.length)
    self.setParam('scale', inventory.scale)
    self.setParam('contrast', inventory.contrast)
    self.setParam('background', inventory.background)


from sans.models.CylinderModel import CylinderModel
CylinderModel.Inventory = Inventory
CylinderModel.__establishInventory__ = __establishInventory__
CylinderModel.__restoreFromInventory__ = __restoreFromInventory__


