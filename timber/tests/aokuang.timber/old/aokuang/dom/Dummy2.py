
# intentionally give attribute and corresponding inventory item different names

class Dummy2(object):

    
    def __init__(self, s=''):
        self.s = s


    def __establishInventory__(self, inventory):
        inventory.s2 = self.s


    def __restoreFromInventory__(self, inventory):
        self.s = inventory.s2



from dsaw.model.Inventory import Inventory as InvBase
class Inventory(InvBase):

    s2 = InvBase.d.str(name='s2', default='')


Dummy2.Inventory = Inventory
