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


from journal.services.Daemon import Daemon as base
from luban.applications.SuperAppForDaemon import SuperAppForDaemon, DaemonInterfaceToPIDStore
class Daemon(DaemonInterfaceToPIDStore, base):

    class Inventory(DaemonInterfaceToPIDStore.Inventory, base.Inventory):
        pass
    

    def _defaults(self):
        super(Daemon, self)._defaults()
        self.inventory.client = "remote"
        return
    

def main():
    superapp = SuperAppForDaemon('journald-harness', Daemon)
    return superapp.run()


# version
__id__ = "$Id$"

# End of file 


