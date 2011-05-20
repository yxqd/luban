
import shapes

class Sample3:

    shape = shapes.AbstractShape()

    weight = 1.0


from dsaw.model.Inventory import Inventory as InvBase
class Inventory(InvBase):
    weight = InvBase.d.float(name='weight')
    shape = InvBase.d.reference(name='shape', targettype=shapes.AbstractShape, targettypes=shapes.all, owned=0)
Sample3.Inventory = Inventory



