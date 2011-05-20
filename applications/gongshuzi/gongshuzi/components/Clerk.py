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
        db = pyre.inventory.str('db', default = '../content/db' )
        dbwrapper = pyre.inventory.str('dbwrapper', default = 'sqlite')
        

    def __init__(self, name = 'clerk', facility = 'clerk'):
        base.__init__(self, name, facility)
        return


    def findParentDocument(self, element, visual, subtree=None):
        parent = self.findParentDocumentByCheckingReferenceSetTable(element)
        if parent: return parent

        if not subtree:
            subtree = visual.visualinstance.dereference(self.db)

        itercontents = subtree.contents.dereference(self.db)
        for name, node in itercontents:
            if node.id == element.id:
                return subtree
            continue

        for name, node in itercontents:
            candidate = self.findParentDocument(element, visual, subtree=node)
            if candidate: return candidate
            continue
        
        return


    def findParentDocumentByCheckingReferenceSetTable(self, element):
        from dsaw.db._referenceset import _ReferenceSetTable
        candidates = element.getReferences(
            self.db,
            table=_ReferenceSetTable,
            refname = 'element',
            containerlabel = 'contents',
            )
        
        if len(candidates)>1: return
        if not candidates: return
        r = candidates[0]
        parent = r.container.dereference(self.db)
        return parent
        

    def indexUsers(self, where=None):
        """create an index of all users that meet the specified criteria"""
        from vnf.dom.User import User
        index = {}
        users = self.db.fetchall(User, where=where)
        for user in users:
            index[user.username] = user
            continue
        return index


    def indexActiveUsers(self):
        return self.indexUsers()


    def getUser(self, username):
        from gongshuzi.dom.User import User
        return self.db.query(User).filter_by(username=username).one()


    def getUserInfo(self, username):
        from gongshuzi.dom.Registrant import Registrant
        return self.db.query(Registrant).filter_by(username=username).one()
        

    def updateRecordWithID(self, record):
        'update a record. assumes that it has a "id" column'
        return self.db.updateRecord(record)


    def getRecordByID(self, tablename, id):
        from pyre.db.Table import Table as TableBase
        if isinstance(tablename, basestring):
            Table = self._getTable(tablename)
        elif issubclass(tablename, TableBase):
            Table = tablename
        else:
            raise ValueError, 'tablename must be a string or a table class: %s' % tablename
        return self._getRecordByID(Table, id)
    
    
    def insertNewOwnedRecord(self, table, owner = None):
        '''create a new record for the given table.

        The given table is assumed to have following fields:
          - id
          - creator
          - date
        '''
        if isinstance(table, str): table = self._getTable(table)
        
        director = self.director
        id = director.getGUID()

        record = table()
        record.id = id

        if not owner: 
            owner = director.sentry.username
        record.creator = owner
        
        self.insertNewRecord( record )
        return record


    def insertNewRecordWithID(self, table):
        '''create a new record for the given table and store it in the db.

        The given table is assumed to have following fields:
          - id
        '''
        record = self.createRecordWithID(table)
        return self.insertNewRecord(record)
    
    
    def createRecordWithID(self, table):
        '''create a new record for the given table but do not store it in the db.

        The given table is assumed to have following fields:
          - id
        '''
        record = table()
        
        director = self.director
        id = director.getGUID()
        record.id = id

        return record


    def insertNewRecord(self, record):
        'insert a new record into db'
        try:
            self.db.insertRow( record )
        except:
            columns = record.getColumnNames()
            values = [ record.getColumnValue( column ) for column in columns ]
            s = ','.join(
                [ '%s=%s' % (column, value)
                  for column, value in zip(columns, values)
                  ] )
            self._debug.log( 'failed to insert record: %s' % s)
            raise
        return record


    def deleteRecordWithID(self, record):
        'delete a record. assumes that it has a "id" column'
        self.db.deleteRecord(record)
        return
    

    def dereference(self, pointer):
        '''dereference a "pointer"'''
        return pointer.dereference(self.db)


    def _getTable(self, name):
        return self.db.getTable(name)


    def _getRecordByID(self, table, id ):
        return self.db.query(table).filter_by(id=id).one()
        

    def _configure(self):
        base._configure(self)
        self.db = self.inventory.db
        self.dbwrapper = self.inventory.dbwrapper
        return


    def _init(self):
        base._init(self)

        from dsaw.db import connect
        url = '%s:///%s' % (self.dbwrapper, self.db)
        self.db = connect(db=url)

        # create orm and register tables
        from gongshuzi.dom import initorm, tables
        orm = initorm()
        self.orm = orm

        # create tables
        for table in list(orm.iterTables())+tables():
            self.db.registerTable(table)
            continue
        self.db.createAllTables()

        return


    def _fini(self):
        base._fini(self)
        return
    

import os
import pickle


# version
__id__ = "$Id$"

# End of file 
