#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                        California Institute of Technology
#                        (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import os
from luban.applications.SimpleHttpServerDaemon import SimpleHttpServerDaemon as base
from luban.applications.SuperAppForDaemon import SuperAppForDaemon as safdbase, DaemonInterfaceToPIDStore
class Daemon(DaemonInterfaceToPIDStore, base):

    class Inventory(DaemonInterfaceToPIDStore.Inventory, base.Inventory):
        pass


    def _defaults(self):
        super(Daemon, self)._defaults()
        self.inventory.home = os.path.abspath('../html')
        return
    

class SuperAppForDaemon(safdbase):

    def _defaults(self):
        super(SuperAppForDaemon, self)._defaults()
        self.inventory.config = [os.path.abspath('../config')]
        return
    

def main():
    superapp = SuperAppForDaemon('simplehttpserver-harness', Daemon)
    return superapp.run()


# version
__id__ = "$Id$"

# End of file 
