#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                             Michael A.G. Aivazis
#                      California Institute of Technology
#                      (C) 1998-2005  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


'''
Script to launch wx UI application
'''


# different from webmain.py, we don't need to hide warnings. 


# this makes assumption of the installation scheme of a luban project
import sys, os
sys.path = [os.path.abspath('..')] + sys.path


from luban.applications.SuperApp import SuperApp as base

class SuperApp(base):


    def _defaults(self):
        super(SuperApp, self)._defaults()

        import os
        from pyre.inventory.odb.prefix import _SYSTEM_ROOT
        lubanappconfig = os.path.join(_SYSTEM_ROOT, 'luban-application')
        
        self.inventory.config =  [
            '../content/components', '../config',
            '/tmp/luban-services',
            lubanappconfig,
            ]
        return
    

def main():
    from luban.applications.WXApplication import WXApplication
    superapp = SuperApp('main', WXApplication)
    return superapp.run()


# version
__id__ = "$Id$"

# End of file 
