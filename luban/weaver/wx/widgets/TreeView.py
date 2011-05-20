#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import wx
from CommonInterface import CommonInterface
from ext import bindCallbacks

import weakref


class TreeView(wx.TreeCtrl, CommonInterface):
    

    def __init__(self, parent, size=(300,300)): # shouldn't hard-code size?
        CommonInterface.__init__(self, parent)
        wx.TreeCtrl.__init__(self, parent, size=size)

        # give the tree container a reference to this tree
        parent.tree = self

        # tooltip
        self.bindToolTipEventHandlerForAllNodes()
        self.bindSelectNodeEventHandlerForAllNodes()
        return


    def getSelection(self):
        return self.GetSelection()


    def addRoot(self, label):
        root = self.AddRoot(label)

        # data
        # data = {}
        # self.SetItemData(root, wx.TreeItemData(data))
        
        # a weak reference from root to tree
        import weakref
        root.tree = weakref.ref(self)

        # a reference from tree to root
        self.root = root
        
        return root


    def addNode(self, referencenode, newnode, position=None):
        if position == 'after':
            parent = self.GetItemParent(referencenode)
            previous = referencenode
            label = newnode.label
            # icon?
            newitem = self.InsertItem(parent, previous, label)

        elif position == 'before':
            parent = self.GetItemParent(referencenode)
            next = self.indexOfChild(parent, referencenode)
            label = newnode.label
            # icon?
            newitem = self.InsertItemBefore(parent, index=next, text=label)

        elif position is None:
            # means to append to the children of the referencenode
            parent = referencenode
            newitem = self.AppendItem(parent, newnode.label)

        elif not isinstance(position, int):
            if not position:
                # same as None
                return self.addNode(referencenode, newnode)
            raise ValueError, 'unknown position: %r(%s)' % (position, type(position))

        else:
            parent = referencenode
            index = position
            label = newnode.label
            newitem = self.InsertItemBefore(referencenode, index=index, text=label)

        # data to accompany the node
        data = {}
        # 1. tip
        if newnode.tip: data['tooltip'] = newnode.tip
        # 2. onclick
        if hasattr(newnode, 'onclick_compiled'): data['onclick'] = newnode.onclick_compiled
        # 
        self.SetItemData(newitem, wx.TreeItemData(data))

        # keep a weak ref to my tree
        newitem.tree = weakref.ref(self)
        
        return newitem
    

    def bindToolTipEventHandlerForAllNodes(self):
        def _(evt):
            item = evt.GetItem()
            if item:
                itemdata = self.GetItemData(item).GetData()
                if itemdata:
                    tooltip = itemdata.get('tooltip')
                    if tooltip:
                        evt.SetToolTip(tooltip)
        self.Bind(wx.EVT_TREE_ITEM_GETTOOLTIP, _)
        return


    def bindSelectNodeEventHandlerForAllNodes(self):
        def _(evt):
            item = evt.GetItem()
            if item:
                itemdata = self.GetItemData(item).GetData()
                if itemdata:
                    func = itemdata.get('onclick')
                    if func:
                        func()
        self.Bind(wx.EVT_TREE_SEL_CHANGED, _)
        return
    

    def indexOfChild(self, parent, child):
        'given child and its parent, find out index of this child in the siblings'
        children = list(iterChildren(self, parent))
        return children.index(child)


    def selectNode(self, node=None):
        return self.SelectItem(node)


    def removeNode(self, node=None):
        if not node:
            # delete the current selected node
            widget = self.GetSelection()
        return self.Delete(node)

#----------------------------------------------------------
# drag and drop helper functions -- causes the nodes to actually move.
# liberally copy-pasted from http://wiki.wxpython.org/DragAndDropWithFolderMovingAndRearranging

    def OnBeginDrag(self, event):
        '''Allow drag-and-drop for leaf nodes.'''
        event.Allow()
        self.dragItem = event.GetItem()

    def OnEndDrag(self, event):

        # If we dropped somewhere that isn't on top of an item, ignore the event
        if event.GetItem().IsOk():
            target = event.GetItem()
        else:
            return

        # Make sure this member exists.
        try:
            source = self.dragItem
        except:
            return

        # Prevent the user from dropping an item inside of itself
        if self.ItemIsChildOf(target, source):
            print "the tree item can not be moved in to itself! "
            self.Unselect()
            return

        # Get the target's parent's ID
        targetparent = self.GetItemParent(target)
        if not targetparent.IsOk():
            targetparent = self.GetRootItem()

        # One of the following methods of inserting will be called...   
        def MoveHere(event):
            # Save + delete the source
            save = self.SaveItemsToList(source)
            self.Delete(source)
            newitems = self.InsertItemsFromList(save, targetparent, target)
            #self.tree.UnselectAll()
            for item in newitems:
                self.SelectItem(item)

        def InsertInToThisGroup(event):
            # Save + delete the source
            save = self.SaveItemsToList(source)
            self.Delete(source)
            newitems = self.InsertItemsFromList(save, target)
            #self.tree.UnselectAll()
            for item in newitems:
                self.SelectItem(item)

        if self.IsExpanded(target):
           InsertInToThisGroup(None)
        else:
           MoveHere(None)


    def Traverse(self, func, startNode):
        """Apply 'func' to each node in a branch, beginning with 'startNode'. """
        def TraverseAux(node, depth, func):
            nc = self.GetChildrenCount(node, 0)
            child, cookie = self.GetFirstChild(node)
            # In wxPython 2.5.4, GetFirstChild only takes 1 argument
            for i in xrange(nc):
                func(child, depth)
                TraverseAux(child, depth + 1, func)
                child, cookie = self.GetNextChild(node, cookie)
        func(startNode, 0)
        TraverseAux(startNode, 1, func)

    def ItemIsChildOf(self, item1, item2):
        ''' Tests if item1 is a child of item2, using the Traverse function '''
        self.result = False
        def test_func(node, depth):
            if node == item1:
                self.result = True

        self.Traverse(test_func, item2)
        return self.result

    def SaveItemsToList(self, startnode):
        ''' Generates a python object representation of the tree (or a branch of it),
            composed of a list of dictionaries with the following key/values:
            label:      the text that the tree item had
            data:       the node's data, returned from GetItemPyData(node)
            children:   a list containing the node's children (one of these dictionaries for each)
        '''
        global list
        list = []

        def save_func(node, depth):
            tmplist = list
            for x in range(0,depth):
                if not type(tmplist[-1]) is dict:
                    tmplist.append({})
                if not tmplist[-1].has_key('children'):
                    tmplist[-1]['children'] = []
                tmplist = tmplist[-1]['children']

            item = {}
            item['label'] = self.GetItemText(node)
            item['data'] = self.GetItemPyData(node)
            item['icon-normal'] = self.GetItemImage(node, wx.TreeItemIcon_Normal)
            item['icon-selected'] = self.GetItemImage(node, wx.TreeItemIcon_Selected)
            item['icon-expanded'] = self.GetItemImage(node, wx.TreeItemIcon_Expanded)
            item['icon-selectedexpanded'] = self.GetItemImage(node, wx.TreeItemIcon_SelectedExpanded)

            tmplist.append(item)

        self.Traverse(save_func, startnode)
        return list

    def InsertItemsFromList(self, itemlist, parent, insertafter=None, appendafter=False):
        ''' Takes a list, 'itemslist', generated by SaveItemsToList, and inserts
            it in to the tree. The items are inserted as children of the
            treeitem given by 'parent', and if 'insertafter' is specified, they
            are inserted directly after that treeitem. Otherwise, they are put at
            the begining.
            
            If 'appendafter' is True, each item is appended. Otherwise it is prepended.
            In the case of children, you want to append them to keep them in the same order.
            However, to put an item at the start of a branch that has children, you need to
            use prepend. (This will need modification for multiple inserts. Probably reverse
            the list.)

            Returns a list of the newly inserted treeitems, so they can be
            selected, etc..'''
        newitems = []
        for item in itemlist:
            if insertafter:
                node = self.InsertItem(parent, insertafter, item['label'])
            elif appendafter:
                node = self.AppendItem(parent, item['label'])
            else:
                node = self.PrependItem(parent, item['label'])
            self.SetItemPyData(node, item['data'])
            self.SetItemImage(node, item['icon-normal'], wx.TreeItemIcon_Normal)
            self.SetItemImage(node, item['icon-selected'], wx.TreeItemIcon_Selected)
            self.SetItemImage(node, item['icon-expanded'], wx.TreeItemIcon_Expanded)
            self.SetItemImage(node, item['icon-selectedexpanded'], wx.TreeItemIcon_SelectedExpanded)

            newitems.append(node)
            if item.has_key('children'):
                self.InsertItemsFromList(item['children'], node, appendafter=True)
        return newitems

    def OnCompareItems(self, item1, item2):
        t1 = self.GetItemText(item1)
        t2 = self.GetItemText(item2)
        self.log.WriteText('compare: ' + t1 + ' <> ' + t2 + '\n')
        if t1 < t2: return -1
        if t1 == t2: return 0
        return 1

# end drag and drop helper functions
#-------------------------------------------

    # bind() is called when 'draggable' is True
    # bind() just allows nodes to be dragged and dropped
    def bind(self):
        self.Bind(wx.EVT_TREE_BEGIN_DRAG, self.OnBeginDrag)
        self.Bind(wx.EVT_TREE_END_DRAG, self.OnEndDrag)

    # bindcallbacks() is called when 'onnodemoving' is some action
    # it binds both the drag and drop capability and the user-defined action
    def bindcallbacks(self, callbackfunc=None):
        self.Bind(wx.EVT_TREE_BEGIN_DRAG, self.OnBeginDrag)

        from ext import bindCallbacks
        events={'drag': wx.EVT_TREE_END_DRAG}

        # put self.OnEndDrag and the user's callback function together
        # in one function to bind to the wx event
        def endDrag(evt):
            self.OnEndDrag(evt)
            callbackfunc(evt)

        totalcallbacks={'drag': endDrag}
        bindCallbacks(self, events, totalcallbacks)


    # for onAppend()
    def addChild(self, child):
        return

    pass # end of TreeView



# helpers
def iterChildren(tree, parent):
    item, cookie = tree.GetFirstChild(parent)
    yield item
    while item.IsOk():
        item, cookie = tree.GetNextChild(parent, cookie)
        yield item
    return


# version
__id__ = "$Id$"

# End of file 
