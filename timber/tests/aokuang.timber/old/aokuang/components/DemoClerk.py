# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from pyre.components.Component import Component as base


class Clerk( base ):

    class Inventory( base.Inventory):

        import pyre.inventory
        db = pyre.inventory.str('db', default = 'db-pickles' )
        

    def __init__(self, name = 'democlerk', facility = 'clerk'):
        base.__init__(self, name, facility)
        return


    def indexActiveUsers(self):
        from aokuang.dom.User import User
        index = {}
        users = self.getRecords(User)
        for key, user in users:
            index[user.username] = user
            continue
        return index


    def getUser(self, username):
        users = self.indexActiveUsers()
        return users[username]


    def getUserInfo(self, username):
        from aokuang.dom.Registrant import Registrant
        registrants = self.getRecords(Registrant)

        candidates = filter(
            lambda r: r[1].username==username, registrants)

        assert len(candidates) < 2

        if not candidates: return
        return candidates[0][1]
        

    def newRecord(self, record):
        tablename = record.name
        store = self._retrieve_store( tablename )
        store[ record.id ] = record
        self._update_store( tablename, store )
        return


    def updateRecord(self, record):
        tablename = record.name
        store = self._retrieve_store( tablename )
        store[ record.id ] = record
        self._update_store( tablename, store )
        return


    def getRecordByID(self, table, id):
        if not isinstance(table, basestring): table = table.name
        store = self._retrieve_store( table )
        return store[ id ]


    def getRecords(self, table):
        if not isinstance(table, basestring): table = table.name
        store = self._retrieve_store(table)
        return store.iteritems()


    def _retrieve_store(self, tablename):
        path = self._store_path( tablename )
        if not os.path.exists( path ):
            ret = dict()
        else:
            f = open(path) 
            ret = pickle.load( f )
            f.close()
            
        return ret


    def _update_store(self, tablename, newstore):
        store = self._retrieve_store( tablename )
        store.update( newstore )
        path = self._store_path(tablename)
        f = open(path, 'w') 
        pickle.dump(store, f)
        f.close()
        return


    def _store_path(self, tablename):
        return os.path.join( self.dbroot, tablename )
    

    def _configure(self):
        base._configure(self)
        self.dbroot = self.inventory.db
        return


    def _init(self):
        base._init(self)
        return


    def _fini(self):
        base._fini(self)
        return
    

import os
import pickle


# version
__id__ = "$Id$"

# End of file 
