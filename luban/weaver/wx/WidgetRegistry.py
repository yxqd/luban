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


import wx


class WidgetRegistry(object):

    def __init__(self):
        self._store = {}
        self.app_globals = None
        return


    def register(self, id, widget):
        id = str(id)
        self._store[id] = widget
        return


    def __call__(self, selector):
        if isinstance(selector, str):
            if selector.startswith('#'):
                return self._proxy(self._getWidgetById(selector[1:]))
        elif isinstance(selector, wx.Window):
            return self._proxy(selector)
        raise NotImplementedError("selector: %s" % selector)


    def _getWidgetById(self, id):
        if id not in self._store:
            raise RuntimeError("widget %r not registered. registered widgets: %s" % (id, self._store))
        return self._store[id]


    def _proxy(self, widget):
        p = widget
        p._globals = self.app_globals
        return p
    
        

# version
__id__ = "$Id$"

# End of file 
