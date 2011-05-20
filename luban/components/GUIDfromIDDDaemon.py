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


# component to generate guid using a client to connects to pyre's idd service
# daemon


from pyre.components.Component import Component
class GUID(Component):

    class Inventory(Component.Inventory):

        import pyre.inventory

        import pyre.idd

        idd = pyre.inventory.facility(
            'idd-session',
            factory=pyre.idd.session,
            args=['idd-session'])
        idd.meta['tip'] = "access to the token server"


    def generate(self):
        return self.idd.token().locator


    def __init__(self, name='guidfromidddaemon', facility='GUID'):
        super(GUID, self).__init__(name, facility)
        return


    def _configure(self):
        super(GUID, self)._configure()
        self.idd = self.inventory.idd
        return


import os


# version
__id__ = "$Id$"

# End of file 
