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


from luban.applications.SuperApp import SuperApp as base

class SuperApp(base):


    def _defaults(self):
        super(SuperApp, self)._defaults()
        self.inventory.config =  ['../content/components', '../config', '/tmp/luban-services']
        return
    


def main():
    from luban.applications.SSHTunnel import SSHTunnel
    superapp = SuperApp('sshtunnel', SSHTunnel)
    return superapp.run()


# version
__id__ = "$Id$"

# End of file 
