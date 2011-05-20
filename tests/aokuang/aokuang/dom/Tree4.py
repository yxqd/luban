
class AbstractNode4:

    pass


class Leaf4(AbstractNode4):

    name = ''


class Branch4(AbstractNode4):

    name = ''

    nodes = [Leaf4()]

    def __init__(self, name='', nodes=None):
        self.name = name
        self.nodes = nodes or []


class Tree4:

    root = Branch4()

    def __init__(self, root):
        self.root = root


nodetypes = [Leaf4, Branch4]



from dsaw.model.Inventory import Inventory as InvBase
class Inventory(InvBase):

    name = InvBase.d.str(name='name')
    nodes = InvBase.d.referenceSet(
        name='nodes', targettype=Leaf4, owned=0)
Branch4.Inventory = Inventory
