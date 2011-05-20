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


class Librarian:

    def __init__(self, cssbase='css', jsbase='javascripts'):
        self.cssbase = cssbase
        self.jsbase = jsbase
        self._registry = {}
        #
        self.register('application', [], [])
        return


    def register(self, widget, stylesheets, jslibs):
        self._registry[widget] = {
            'css': map(self._csspath, stylesheets),
            'js': map(self._jspath, jslibs),
            }
        return


    def iterWidgets(self):
        return self._registry.iterkeys()
        

    def getStyleSheets(self, widget=None):
        return self._registry[widget]['css']


    def getJavaScriptLibs(self, widget=None):
        return self._registry[widget]['js']


    def _csspath(self, stylesheet):
        path = [self.cssbase, stylesheet]
        return '/'.join(path)
        
        
    def _jspath(self, jslib):
        path = [self.jsbase, jslib]
        return '/'.join(path)


# version
__id__ = "$Id$"

# End of file 
