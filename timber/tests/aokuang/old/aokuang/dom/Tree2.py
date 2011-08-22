
class AbstractNode:

    pass


class Leaf(AbstractNode):

    name = ''


class Branch2(AbstractNode):

    name = ''

    nodes = [AbstractNode()]

    def __init__(self, name='', nodes=None):
        self.name = name
        self.nodes = nodes or []


class Tree2:

    root = Branch2()

    def __init__(self, root):
        self.root = root


nodetypes = [Leaf, Branch2]



from dsaw.model.Inventory import Inventory as InvBase
class Inventory(InvBase):

    name = InvBase.d.str(name='name')
    nodes = InvBase.d.referenceSet(
        name='nodes', targettype=Leaf, owned=1)
Branch2.Inventory = Inventory
