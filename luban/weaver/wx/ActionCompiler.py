# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


class ActionCompiler(object):


    widgetweaver = None


    def setGlobals(self, globals):
        self._globals = globals
        self.createClient()
        return


    def createClient(self):
        A = self._globals['A']
        from .Client import Client
        self.client = Client(A)
        return


    def compile(self, actions, this=None):
        
        if not actions: return []
        
        if '__iter__' not in dir(actions):
            actions = [actions]
            
        for action in actions:
            self.render(action)
            continue

        return

    
    def render(self, action):
        return action.identify(self)

        
    def onLoading(self, loading):
        actor = loading.actor
        routine = loading.routine
        params = loading.params
        self.client.load(actor, routine=routine, **params)
        return


    def onSubmission(self, submission):
        form = submission.form
        wxformproxy = form.identify(self)
        wxformproxy.clearErrors()

        actor = submission.actor
        routine = submission.routine
        params = submission.params
        self.client.submit(wxformproxy, actor, routine=routine, **params)
        return
    

    def onSelectByID(self, selector):
        id = selector.id
        W = self._globals['W']
        return W('#'+str(id))


    def onSelectByElement(self, selector):
        element = selector.element
        id = element.id
        W = self._globals['W']
        return W('#'+str(id))

    
    def onReplaceContent(self, replace):
        element = replace.element
        e = element.identify(self)
        e.empty()
        
        newcontent = replace.newcontent
        A = self._globals['A']
        new = self.widgetweaver.weave(
            newcontent, container=e, appglobals=A._globals)

        debug.log('new=%s' % new)
        e.addChild(new)
        e.fitall()
        return


    def onRemoveContent(self, removal):
        element = removal.element
        e = element.identify(self)
        return e.empty()


    def onSimpleAction(self, action):
        params = action.params
        name = action.actionname
        handler = getattr(self, 'on'+name)
        return handler(params)


    def onSimpleElementAction(self, action):
        if action.actionname == 'setAttribute':
            return self.onSetAttribute(action)

        element = action.element
        element = self.render(element)

        actionname = action.actionname
        try:
            method = getattr(element, actionname)
        except AttributeError as e:
            raise RuntimeError("Unable to compile simpleelementaction: actioname=%s, element=%s" % (actionname, element))
        return method(**action.params)


    def onAppendElement(self, action):
        container = action.container
        child = action.element
        containerelement = container.identify(self)
        A = self._globals['A']
        new = self.widgetweaver.weave(
            child,
            container=containerelement,
            appglobals=A._globals)

        # do this to catch the exceptions appmenu and treeview throw
        try:
            containerelement.addChild(new)
            containerelement.fitall()
        except:
            pass

        return


    def onalert(self, alert):
        import wx
        wx.MessageBox(alert['message'], 'Alert', wx.OK)
        return


    def onNotification(self, notification):
        element = notification.element.identify(self)
        return self.client.notify(
            element = element,
            evtname = notification.event,
            actor = notification.actor, routine = notification.routine,
            **notification.params)


    def onSetAttribute(self, action):
        selectedelement = action.element.identify(self)
        selectedelement.setAttribute(**action.params)
        return


    # treeview
    def onTreeViewRemoveNode(self, action):
        treeview = action.treeview.identify(self)
        node = action.node.identify(self)
        treeview.removeNode(node)
        return


    def onTreeViewSelectNode(self, action):
        treeview = action.treeview.identify(self)
        node = action.node.identify(self)
        treeview.selectNode(node)
        return


    def onTreeViewAddBranch(self, action):
        treeview = action.treeview.identify(self)
        referencenode = action.referencenode.identify(self)

        # need to compile actions for new node
        newnode = action.newnode
        def _(): self.compile(newnode.onclick)
        newnode.onclick_compiled = _
        
        node = treeview.addNode(referencenode, action.newnode, action.position)
        

from ._journals import *

# version
__id__ = "$Id$"

# End of file 
