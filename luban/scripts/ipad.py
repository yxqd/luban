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


# this makes assumption of the installation scheme of a luban project
import sys, os
sys.path = [os.path.abspath('..')] + sys.path


from luban.applications.SuperAppForDaemon import SuperAppForDaemon as safdbase, DaemonInterfaceToPIDStore
from pyre.ipa.Daemon import Daemon as base
class Daemon(DaemonInterfaceToPIDStore, base):

    class Inventory(DaemonInterfaceToPIDStore.Inventory, base.Inventory):
        pass



class SuperAppForDaemon(safdbase):

    def _defaults(self):
        super(SuperAppForDaemon, self)._defaults()
        self.inventory.config = ['../config']
        return


def main():
    superapp = SuperAppForDaemon('ipa-harness', Daemon)
    return superapp.run()


# version
__id__ = "$Id$"

# End of file 
