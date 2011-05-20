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


from pyre.components.Component import Component as base

class Weaver(base):

    class Inventory(base.Inventory):

        import pyre.inventory
        
        from ActionCompiler import ActionCompiler
        action_compiler = pyre.inventory.facility(
            'action-compiler', factory=ActionCompiler)


    def weave(self, document, **kwds):
        return self.weaver.render(document, **kwds)


    def compile(self, action):
        return self.weaver.compile(action)


    def __init__(self, name='wx-weaver', facility='weaver'):
        super(Weaver, self).__init__(name, facility)
        return


    def _configure(self):
        super(Weaver, self)._configure()
        self.action_compiler = self.inventory.action_compiler
        return
    

    def _init(self):
        super(Weaver, self)._init()
        from luban.weaver.wx.Weaver import Weaver as factory
        weaver = factory(self.action_compiler)
        self.weaver = weaver

        # action compiler needs widget weaver
        self.action_compiler.setWidgetWeaver(self)
        return


# version
__id__ = "$Id$"

# End of file 
