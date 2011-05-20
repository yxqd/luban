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


from pyre.components.Component import Component

class ActionCompiler(Component):

    def compile(self, actions, **kwds):
        return self.compiler.compile(actions, **kwds)


    def setGlobals(self, globals):
        self.compiler.setGlobals(globals)
        return


    def setWidgetWeaver(self, weaver):
        self.compiler.widgetweaver = weaver
        return
    

    def __init__(self):
        super(ActionCompiler, self).__init__('wx-action-compiler', 'action-compiler')
        return


    def _init(self):
        super(ActionCompiler, self)._init()
        from luban.weaver.wx.ActionCompiler import ActionCompiler as factory
        self.compiler = factory()
        return
    

# version
__id__ = "$Id$"

# End of file 
