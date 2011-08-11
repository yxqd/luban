# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



from .Element import Element, Meta

from .ElementNotRoot import ElementNotRoot
class TreeViewLeaf(ElementNotRoot, Element, metaclass=Meta):

    abstract = False


    label = descriptors.str()
    icon = descriptors.str()
    tip = descriptors.str()
    onclick = descriptors.action()
    
    def __init__(self, *args, **kwds):
        Element.__init__(self, *args, **kwds)
        return
    

    def identify(self, visitor):
        return visitor.onTreeViewLeaf( self )


from .ElementContainer import ElementContainer, Meta as ECMeta

class TreeViewBranch(ElementNotRoot, ElementContainer, metaclass=ECMeta):

    abstract = False


    label = descriptors.str()
    icon = descriptors.str()
    tip = descriptors.str()
    onclick = descriptors.action()


    def __init__(self, *args, **kwds):
        ElementContainer.__init__(self, *args, **kwds)
        return
    

    def branch(self, *args, **kwds):
        b = TreeViewBranch(*args, **kwds)
        self.append(b)
        return b


    def leaf(self, *args, **kwds):
        l = TreeViewLeaf(*args, **kwds)
        self.append(l)
        return l


    def identify(self, renderer):
        return renderer.onTreeViewBranch(self)
        


class TreeView(ElementContainer):


    abstract = False


    root = descriptors.element()

    draggable = descriptors.bool()
    
    onclick = descriptors.action()
    onnodemoving = descriptors.action()

    # obsolete
    label = descriptors.str()
    
    def __init__(self, **kwds):
        if 'label' in kwds:
            warnings.warn("Attribute 'label' is no longer supported", DeprecationWarning)
        ElementContainer.__init__(self, **kwds)
        return


    def setRoot(self, *args, **kwds):
        self.root = TreeViewBranch(*args, **kwds)
        return self.root


    def identify(self, visitor):
        return visitor.onTreeView(self)



from .Action import Action
class TreeViewSetRoot(Action):

    abstract = False


    treeview = descriptors.object()
    root = descriptors.object()
    
    
class TreeViewRemoveNode(Action):

    abstract = False


    treeview = descriptors.object()
    node = descriptors.object()
    

    def identify(self, inspector):
        return inspector.onTreeViewRemoveNode(self)

    
    
class TreeViewSelectNode(Action):

    abstract = False


    treeview = descriptors.object()
    node = descriptors.object()
    
    def identify(self, inspector):
        return inspector.onTreeViewSelectNode(self)


    
class TreeViewAddBranch(Action):

    abstract = False


    treeview = descriptors.object()
    referencenode = descriptors.object()
    newnode = descriptors.object()
    position = descriptors.str()

    def __init__(self, treeview=None, referencenode=None, newnode=None, position=None):
        Action.__init__(self)
        self.treeview = treeview
        self.referencenode = referencenode
        self.newnode = newnode
        self.position = position or ''
        return


    def identify(self, inspector):
        return inspector.onTreeViewAddBranch(self)




import warnings
class TreeViewActions:

    def setTreeViewRoot(self, root):
        warnings.warn("element.setTreeViewRoot is obsolete, please use element.treeview('setRoot', root=...)", DeprecationWarning)
        return TreeViewSetRoot(treeview=self, root=root)
        

    def addTreeViewBranch(self, referencenode, newnode, position=None):
        warnings.warn("element.addTreeViewBranch is obsolete, please use element.treeview('addBranche', referencenode=..., newnode=..., position=...)", DeprecationWarning)
        if isinstance(referencenode, str):
            warnings.warn("element.addTreeViewBranch(..., referencenode=<reference id>, ...) is obsolete, please use element.treeview('addBranch', referencenode=<reference node selector>, newnode=<new branch instance>, position=<position string>)", DeprecationWarning)
            from luban.content import select
            referencenode = select(id=referencenode)
        return TreeViewAddBranch(self, referencenode, newnode, position=position)
    

    def removeTreeViewNode(self, node):
        warnings.warn("element.removeTreeViewNode is obsolete, please use element.treeview('removeNode', node=...)", DeprecationWarning)
        if isinstance(node, str):
            warnings.warn("element.removeTreeViewNode(node=<node id>) is obsolete, please use element.treeview('removeNode', node=<node selector>)", DeprecationWarning)
            from luban.content import select
            node = select(id=node)
        return TreeViewRemoveNode(treeview=self, node=node)
    
    
    nontrivial_action_types = [
        'setRoot',
        'addBranch',
        'removeNode',
        'selectNode',
        ]
    
    def treeview(self, actionname, **kwds):
        if actionname in self.__class__.nontrivial_action_types:
            factory = eval('TreeView' + actionname[0].upper()+actionname[1:])
            return factory(treeview=self, **kwds)

        # treeview('select', ...) is obsolete
        if actionname == 'select':
            warnings.warn("element.treeview('select', ...) is obsolete, please use element.treeview('selectNode', node=...)", DeprecationWarning)
            branch = kwds.get('branch')
            node = kwds.get('node')
            if branch and node: raise RuntimeError
            if branch: del kwds['branch']; kwds['node'] = branch
            actionname = 'selectNode'

            node = kwds['node']
            if isinstance(node, str):
                warnings.warn("element.treeview('select', node/branch=<node id>) is obsolete, please use element.treeview('selectNode', node=<node selector>)", DeprecationWarning)
                from luban.content import select
                kwds['node'] = select(id=node)
            return self.treeview(actionname, **kwds)
        
        from .SimpleElementAction import SimpleElementAction
        return SimpleElementAction(self, actionname, **kwds)
    
    

#from ElementActionExtensions import extensions
#extensions.append(TreeViewActions)


# version
__id__ = "$Id$"

# End of file 
