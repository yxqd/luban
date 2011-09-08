
import shapes

class Sample4:

    shape = shapes.Cylinder()
    weight = 1.0


    def __str__(self):
        return 'Sample4(shape=%s, weight=%s)' % (self.shape, weight)


from dsaw.model.Inventory import Inventory as InvBase
class Inventory(InvBase):
    weight = InvBase.d.float(name='weight')
    shape = InvBase.d.reference(name='shape', targettype=shapes.Cylinder, owned=1)
Sample4.Inventory = Inventory



