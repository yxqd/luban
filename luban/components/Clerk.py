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


class Clerk( base ):

    class Inventory( base.Inventory):

        import pyre.inventory
        db = pyre.inventory.str('db', default = '../content/db.sqlite' )
        engine = pyre.inventory.str('engine', default = 'sqlite')
        uri = pyre.inventory.str('uri', default = '')
        

    def __init__(self, name = 'clerk', facility = 'clerk'):
        base.__init__(self, name, facility)
        return


    def _getOrmManager(self):
        if '_orm' not in self.__dict__:
            self._createOrmManager()
        return self._orm
    orm = property(_getOrmManager)


    def _createOrmManager(self):
        director = self.director
        guid = director.getGUID
        db = self.db
        object2table = self._getObject2TableMapper()
        from dsaw.model.visitors.OrmManager import OrmManager
        self._orm = OrmManager(db=db, guid=guid, object2table=object2table)
        return


    def _getObject2TableMapper(self):
        "reload this to provide application-specific mapper"
        return None

    
    def _getTable(self, name):
        return self.db.getTable(name)


    def _getRecordByID(self, table, id ):
        return self.db.query(table).filter_by(id=id).one()


    def _getDB(self):
        if not "_db" in self.__dict__:
            self._db = self._createDB()
        return self._db
    db = property(_getDB)


    def _createDB(self):
        uri = self.inventory.uri
        if not uri:
            engine = self.inventory.engine
            db = self.inventory.db
            uri = '%s:///%s' % (engine, db)
        from dsaw.db import connect
        return connect(db=uri)
        


# version
__id__ = "$Id$"

# End of file 
