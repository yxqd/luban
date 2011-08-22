
import shapes

class Sample2:

    shape = shapes.Cylinder()
    weight = 1.0


    def __str__(self):
        return 'Sample2(shape=%s, weight=%s)' % (self.shape, weight)


from dsaw.model.Inventory import Inventory as InvBase
class Inventory(InvBase):
    weight = InvBase.d.float(name='weight')
    shape = InvBase.d.reference(name='shape', targettype=shapes.Cylinder, owned=0)
Sample2.Inventory = Inventory



