# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from UIApp import UIApp as Base


class WXApplication(Base):


    class Inventory(Base.Inventory):
        
        import pyre.inventory


    def redirect(self, actor, routine, **kwds):
        self.inventory.routine = routine
        self.actor = self.retrieveActor(actor)
        
        if self.actor is not None:
            self.configureComponent(self.actor)
            for k,v in kwds.iteritems():
                setattr(self.actor.inventory, k, v)

        return self.main()


    def render(self, page=None):
        from luban.content.Page import Page
        from luban.content.Element import Element
        from luban.content.Action import Action
        
        if isinstance(page, Page):
            wxapp = self._createWxApp()
            wxframe = self.weaver.weave(
                document=page, container=wxapp, appglobals=self._globals)
            wxapp.start()
        elif isinstance(page, Element):
            wxwidget = self.weaver.weave(
                document=page, container=self._container_widget, appglobals=self._globals)
            return wxwidget
        elif isinstance(page, Action):
            return self.weaver.compile(page)
        elif '__iter__' in dir(page):
            for item in page: self.render(item)
        elif isinstance(page, basestring):
            # is this really the right thing to do?
            print page
        else:
            return page


    def _createWxApp(self):
        from luban.weaver.wx.widgets import app
        return app(self.name)
    

    def __init__(self, name):
        Base.__init__(self, name)
        return


    def _defaults(self):
        super(WXApplication, self)._defaults()
        from luban.components.weaver.wx import weaver
        self.inventory.weaver = weaver()
        return


    def _configure(self):
        super(WXApplication, self)._configure()
        return


    def _init(self):
        super(WXApplication, self)._init()
        
        self._globals = {}
        
        from luban.weaver.wx.WidgetRegistry import WidgetRegistry
        W = WidgetRegistry()
        W.app_globals = self._globals

        self._globals['A'] = self
        self._globals['W'] = W
        return



if __name__=='__main__':
    w=WXApplication(name='test')
    print w

# version
__id__ = "$Id$"

# End of file 
