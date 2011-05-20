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


from luban.content import select, load, alert


from pyre.components.Component import Component as base


class Painter(base):


    class Inventory(base.Inventory):

        import pyre.inventory

        from ObjectPainter import ObjectPainter
        object_painter = pyre.inventory.facility(name='object_painter', factory=ObjectPainter)
    

    def __init__(self, name='painter'):
        super(Painter, self).__init__(name=name, facility = 'painter')
        return


    def _getObjectPainter(self):
        op = self.inventory.object_painter
        orm = self.orm
        op.orm = orm
        return op.engine
    paintObj = property(_getObjectPainter)


    def _getOrmManager(self):
        return self.director.clerk.orm
    orm = property(_getOrmManager)


    def _getObject2FormFields(self):
        director = self.director
        orm = director.clerk.orm
        from luban.orm.Object2FormFields import Object2FormFields
        return Object2FormFields(orm)
    obj2formfields = property(_getObject2FormFields)
    o2flds = obj2formfields


    def _getObject2Form(self):
        r = self.o2flds
        from luban.orm.Object2Form import Object2Form
        return Object2Form(r)
    obj2form = property(_getObject2Form)
    o2fm = obj2form


# version
__id__ = "$Id$"

# End of file 
