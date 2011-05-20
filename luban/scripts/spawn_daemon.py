#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                  Jiao Lin
#                      California Institute of Technology
#                        (C) 2008  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from luban.applications.SuperAppForDaemon import SuperAppForDaemon as safdbase
from luban.applications.LaunchDetached import Launch


class SuperAppForDaemon(safdbase):

    def _defaults(self):
        super(SuperAppForDaemon, self)._defaults()
        self.inventory.config = ['../config', '/tmp/luban-services']
        return


    def help(self):
        import sys, os
        executable = sys.argv[0]
        executable = os.path.basename(executable)
        print
        print 'daemonize the given command <cmd>. It will run at the given directory <home>.'
        print
        print '* Normal usage:' 
        print '  $ %s -home=<home> -cmd=<cmd>' % executable
        print
        print '* Debug mode:'
        print '  $ %s -debug --- -home=<home> -cmd=<cmd>' % executable
        print
        print '* Stop:'
        print '  $ %s -home=<home> -cmd=<cmd> -stop' % executable
        print 
        


def main():
    superapp = SuperAppForDaemon('spawn-daemon', Launch)
    return superapp.run()


# version
__id__ = "$Id$"

# End of file 
