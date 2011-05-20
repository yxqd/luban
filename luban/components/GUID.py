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


# component to generate guid using pyre's idd service implementation
# (not using the service daemon)


from pyre.components.Component import Component
class GUID(Component):

    class Inventory(Component.Inventory):

        import pyre.inventory

        import pyre.idd
        locator = pyre.inventory.facility("recordLocator", factory=pyre.idd.recordLocator)

        datastore_path = pyre.inventory.str('datastore-path', default='../config/guid.dat')


    def generate(self):
        tid = self.tid
        date = self._getDate()
        locator = self.locator.encode(tid, date)

        self._info.log("issued token: ticket id=%s, date=%s, locator=%s" % (
            tid, date, locator))
        self.tid += 1

        return locator


    def __init__(self, name='guid', facility='GUID'):
        super(GUID, self).__init__(name, facility)
        self.tid = None
        return


    def _loadData(self):
        if not os.path.exists(self.datastore_path):
            self.tid = 0
            self._saveData()
        else:
            self.tid = int(open(self.datastore_path).read())
        return


    def _saveData(self):
        if self.tid:
            import os
            dir = os.path.dirname(self.datastore_path)
            if not os.path.exists(dir): os.makedirs(dir)
            open(self.datastore_path, 'w').write(str(self.tid))
        return
        

    def _getDate(self):
        import time
        tick = time.localtime()
        return time.strftime("%y%m%d", tick)

    
    def _configure(self):
        super(GUID, self)._configure()
        self.locator = self.inventory.locator
        self.datastore_path = self.inventory.datastore_path
        return


    def _init(self):
        super(GUID, self)._init()
        self._loadData()
        return


    def _fini(self):
        self._saveData()
        super(GUID, self)._fini()
        return


import os


# version
__id__ = "$Id$"

# End of file 
