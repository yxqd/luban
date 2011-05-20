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


'''
The web interface UI application
'''


from luban.applications.utils import ignoreWarnings
ignoreWarnings()


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
    import journal,os
    debug = journal.debug('main' )
    debug.log(os.environ.get('PATH') )
    debug.log(os.environ.get('PYTHONPATH') )
    
    from luban.applications.CliApplication import CliApplication
    superapp = SuperApp('main', CliApplication)
    return superapp.run()


# version
__id__ = "$Id$"

# End of file 
