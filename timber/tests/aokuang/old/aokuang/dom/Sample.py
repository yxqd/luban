
import shapes

class Sample:

    shape = shapes.AbstractShape()

    weight = 1.0


from dsaw.model.Inventory import Inventory as InvBase
class Inventory(InvBase):
    weight = InvBase.d.float(name='weight')
    shape = InvBase.d.reference(name='shape', targettype=shapes.AbstractShape, targettypes=shapes.all, owned=1)
Sample.Inventory = Inventory



def customizeDrawer(self, drawer):
    drawer.sequence = [
        'shape',
        'properties'
        ]
    drawer.mold.sequence = [
        'weight',
        ]
Sample.customizeLubanObjectDrawer = customizeDrawer
