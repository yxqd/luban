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


from pyre.components.Component import Component as base


class ObjectPainter(base):

    orm = None # director must assign orm to this object painter to make it work
    
    class Inventory(base.Inventory):

        import pyre.inventory
        actor_formatter = pyre.inventory.str(name='actor_formatter', default='orm/%s')
    

    def __init__(self, name='object-painter'):
        super(ObjectPainter, self).__init__(name=name, facility = 'objectpainter')
        return


    def _getEngine(self):
        if hasattr(self, '_engine'): return self._engine
        e = self._engine = self._createEngine()
        return e
    engine = property(_getEngine)

    
    def _getDrawers(self):
        engine = self.engine
        return engine.drawers
    drawers = property(_getDrawers)


    def _createEngine(self):
        af = self._make_actor_formatter()
        from luban.orm.views.ObjectPainter import ObjectPainter
        return ObjectPainter(self.orm, af)


    def _make_actor_formatter(self):
        orm = self.orm
        formatstr = self.inventory.actor_formatter
        def _(Object):
            return formatstr % orm(Object).getTableName()
        return _

    
    
# version
__id__ = "$Id$"

# End of file 
