
class AbstractNode3:

    pass


class Leaf3(AbstractNode3):

    name = ''


class Branch3(AbstractNode3):

    name = ''

    nodes = [AbstractNode3()]

    def __init__(self, name='', nodes=None):
        self.name = name
        self.nodes = nodes or []


class Tree3:

    root = Branch3()

    def __init__(self, root):
        self.root = root


nodetypes = [Leaf3, Branch3]



from dsaw.model.Inventory import Inventory as InvBase
class Inventory(InvBase):

    name = InvBase.d.str(name='name')
    nodes = InvBase.d.referenceSet(
        name='nodes', targettype=AbstractNode3, targettypes=nodetypes, owned=0)
Branch3.Inventory = Inventory
