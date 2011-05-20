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

from luban.applications.SuperAppForDaemon import SuperAppForDaemon, DaemonInterfaceToPIDStore


from pyre.idd.Daemon import Daemon as base
class Daemon(DaemonInterfaceToPIDStore, base):

    class Inventory(DaemonInterfaceToPIDStore.Inventory, base.Inventory):
        pass


def main():
    superapp = SuperAppForDaemon('idd-harness', Daemon)
    return superapp.run()


# version
__id__ = "$Id$"

# End of file 
