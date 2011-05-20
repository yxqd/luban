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


class ObjectPainter:


    def __call__(self, obj):
        return self.drawers.getDrawer(obj.__class__)(obj)


    def __init__(self, orm, actor_formatter):
        self.orm = orm
        self.actor_formatter = actor_formatter
        self.drawers = Drawers(orm, actor_formatter)
        return
    

    pass # end of ObjectDrawer



class Drawers(object):


    def __init__(self, orm, actor_formatter):
        self.orm = orm
        self.actor_formatter = actor_formatter
        self._store = {}
        return
    

    def getDrawer(self, Object):
        if self._store.has_key(Object):
            return self._store[Object]
        r = self._createDefaultDrawer(Object)
        self.setDrawer(Object, r)
        return r


    def setDrawer(self, Object, drawer):
        self._store[Object] = drawer
        return drawer


    def _createDefaultDrawer(self, Object):
        actor_formatter = self.actor_formatter
        actor = actor_formatter(Object)
        from EmbeddedPanelsForComposite import EmbeddedPanelsForComposite
        drawer = EmbeddedPanelsForComposite(self, self.orm, actor, actor_formatter)
        return drawer



# version
__id__ = "$Id$"

# End of file 
