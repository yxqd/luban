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


from luban.components.Clerk import Clerk as base


class Clerk( base ):

    class Inventory( base.Inventory):

        import pyre.inventory
        

    def __init__(self, name = 'democlerk', facility = 'clerk'):
        base.__init__(self, name, facility)
        return


    def indexActiveUsers(self):
        from jazzclub.dom.User import User
        index = {}
        users = self.getRecords(User)
        for user in users:
            index[user.username] = user
            continue
        return index


    def getUser(self, username):
        db = self.db
        from jazzclub.dom.User import User
        return db.query(User).filter_by(username=username).one()


    def getUserInfo(self, username):
        db = self.db
        from jazzclub.dom.Registrant import Registrant
        candidates = db.query(Registrant).filter_by(username=username).all()
        if not candidates: return
        assert len(candidates) == 1
        return candidates[0]
        

    def newRecord(self, record):
        db = self.db
        db.insertRow(record)
        return


    def updateRecord(self, record):
        return self.db.updateRecord(record)


    def getRecordByID(self, table, id):
        return self._getRecordByID(table, id)


    from dsaw.db.Table import Table as TableBase
    def getRecords(self, table):
        db = self.db
        if not issubclass(table, self.TableBase):
            table = self._getTable(table)
        return db.query(table).all()


    def _getTable(self, name):
        try:
            return self._importTable(name)
        except:
            import traceback
            tb = traceback.format_exc()
            self._debug.log(tb)
            pass
        return super(Clerk, self)._getTable(name)


    def _importTable(self, name):
        pkg = 'jazzclub.dom'
        tokens = name.split('.'); module = '.'.join(tokens[:-1]); symbol = tokens[-1]
        fullname = '%s.%s' % (pkg, module)
        return getattr(__import__(fullname, {}, {}, ['']), symbol)


    def _defaults(self):
        super(Clerk, self)._defaults()
        self.inventory.db = 'aokuang.sqlite'
        return
    

import os
import pickle


# version
__id__ = "$Id$"

# End of file 
