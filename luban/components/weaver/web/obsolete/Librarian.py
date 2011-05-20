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

class Librarian(Component):

    class Inventory(Component.Inventory):

        import pyre.inventory

        from Library import Library
        library = pyre.inventory.facility(name='library', factory=Library)
        
        cssbase = pyre.inventory.str(name='cssbase', default='css')
        jsbase = pyre.inventory.str(name='jsbase', default='javascripts')


    def iterWidgets(self):
        return self.librarian.iterWidgets()
        

    def getStyleSheets(self, **kwds):
        return self.librarian.getStyleSheets(**kwds)
    

    def getJavaScriptLibs(self, **kwds):
        return self.librarian.getJavaScriptLibs(**kwds)


    def __init__(self):
        super(Librarian, self).__init__('librarian', 'librarian')
        return


    def _configure(self):
        super(Librarian, self)._configure()
        self.library = self.inventory.library
        self.cssbase = self.inventory.cssbase
        self.jsbase = self.inventory.jsbase
        return


    def _init(self):
        super(Librarian, self)._init()
        from luban.weaver.web.Librarian import Librarian as factory
        self.librarian = factory(cssbase=self.cssbase, jsbase=self.jsbase)
        self._readLibrary()
        return


    def _readLibrary(self):
        lib = self.library

        from Library import categories
        for category in categories:
            cat = getattr(lib, category)
            stylesheets = cat.stylesheets
            javascripts = cat.javascripts
            if category == 'base':
                widget = ''
            else:
                widget = category
                
            if stylesheets or javascripts:
                self.librarian.register(widget, stylesheets, javascripts)
            continue
        return            


# version
__id__ = "$Id$"

# End of file 
