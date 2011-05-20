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


from pyre.weaver.Weaver import Weaver as base

class Weaver(base):

    class Inventory(base.Inventory):

        import pyre.inventory
        
        controllerurl = pyre.inventory.str(
            'controller-url', default = 'cgi-bin/main.py')

        htmlbase = pyre.inventory.str(
            'html-base', default = '/')

        statichtmlbase = pyre.inventory.str('html-static-base', default='')
        cssbase = pyre.inventory.str('css-base', default='css')
        jsbase = pyre.inventory.str('javascripts-base', default='javascripts')
        imagesbase = pyre.inventory.str('images-base', default='images')

        cookie_path = pyre.inventory.str(
            'cookie-path', default = '/cgi-bin/')

        use_cookie = pyre.inventory.bool(
            'use-cookie', default = False)


        from Library import Library
        library = pyre.inventory.facility(name='library', factory=Library)
        

    def resetRenderer(self):
        from luban.weaver.web import create as createWeaver
        renderer = createWeaver(
            htmlbase = self.inventory.htmlbase,
            controller_url = self.inventory.controllerurl,
            statichtmlbase = self.inventory.statichtmlbase,
            cssbase = self.inventory.cssbase,
            jsbase = self.inventory.jsbase,
            imagesbase = self.inventory.imagesbase,
            cookie_path = self.inventory.cookie_path,
            use_cookie = self.inventory.use_cookie,
            output_as_lines = True,
            )
        self.renderer = renderer
        self.librarian = renderer.librarian
        self._readLibrary()
        return


    def __init__(self, name='web-weaver', facility='weaver'):
        super(Weaver, self).__init__(name=name)#, facility=facility)
        return


    def _configure(self):
        super(Weaver, self)._configure()
        self.htmlbase = self.inventory.htmlbase
        self.controllerurl = self.inventory.controllerurl
        self.statichtmlbase = self.inventory.statichtmlbase
        self.cssbase = self.inventory.cssbase
        self.jsbase = self.inventory.jsbase
        self.imagesbase = self.inventory.imagesbase
        self.cookie_path = self.inventory.cookie_path
        self.use_cookie = self.inventory.use_cookie
        return


    def _readLibrary(self):
        librarian = self.librarian
        
        lib = self.inventory.library

        categories = lib.categories
        for category in categories:
            cat = getattr(lib, category)
            stylesheets = cat.stylesheets
            javascripts = cat.javascripts
            if stylesheets or javascripts:
                self.librarian.register(category, stylesheets, javascripts)
            continue
        return

# version
__id__ = "$Id$"

# End of file 
