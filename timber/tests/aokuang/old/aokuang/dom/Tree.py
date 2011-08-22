
class AbstractNode:

    pass


class Leaf(AbstractNode):

    name = ''


class Branch(AbstractNode):

    name = ''

    nodes = [AbstractNode()]

    def __init__(self, name='', nodes=None):
        self.name = name
        self.nodes = nodes or []


class Tree:

    root = Branch()

    def __init__(self, root):
        self.root = root


nodetypes = [Leaf, Branch]



from dsaw.model.Inventory import Inventory as InvBase
class Inventory(InvBase):

    name = InvBase.d.str(name='name')
    nodes = InvBase.d.referenceSet(
        name='nodes', targettype=AbstractNode, targettypes=nodetypes, owned=1)
Branch.Inventory = Inventory
