#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2008  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


'''
Use this script to launch a script (shell, python, ...).
The launched script will be running on a different process
running independently.

 * hint: use -debug to debug this script

A few files will be created from this script in the directory
specified by the "home" property:

 * <sig>.info:  info about the detached process: command and home
 * <sig>.out:   output of the detached process
 * <sig>.err:   error output of the detached process
 * <sig>.pid:   process id of the detached process

'''

from pyre.applications.Daemon import Daemon as Stager
from pyre.applications.Application import Application
from SuperAppForDaemon import DaemonInterfaceToPIDStore

class Launch(DaemonInterfaceToPIDStore, Application, Stager):

    class Inventory(DaemonInterfaceToPIDStore.Inventory, Application.Inventory):

        import pyre.inventory
        home = pyre.inventory.str('home', default = '/tmp')
        cmd = pyre.inventory.str('cmd', default = '')


    def execute(self, *args, **kwds):
        import os
        identifier = self._identifier()
        kwds['stdout'] = os.path.join(self.home, '%s.out' % identifier)
        kwds['stderr'] = os.path.join(self.home, '%s.err' % identifier)
        open(os.path.join(self.home, '%s.info' % identifier), 'w').write(
            'cmd=%s\nhome=%s\n' % (self.cmd, self.home)
            )        
        super(Launch, self).execute(*args, **kwds)
        return
        

    def main(self, *args, **kwds):
        # the command to run
        cmd = self.inventory.cmd
        self._debug.activate()
        self._debug.log( 'cmd=%r' % cmd )
        
        self._debug.log( 'curdir=%r' % os.path.abspath(os.curdir))
        
        # run the command
        # use execvp to make sure the command is run using the same process id
        # the daemon has forked
        import shlex
        args = shlex.split(cmd)
        f = args[0]
        self._debug.log('cmd=%s, args=%s' % (f, args))
        os.execvp(f, args)
        return


    def _configure(self):
        Application._configure(self)
        self.home = os.path.abspath(self.inventory.home)
        self.cmd = self.inventory.cmd
        return

    
    def _pidstore_path(self):
        import os
        cmd = self.inventory.cmd
        cmd = os.path.split(cmd)[-1]
        identifier = self._identifier()
        return os.path.join(self.home, '%s.pid' % identifier)


    def _identifier(self):
        import hashlib
        key = self.cmd + self.home
        self._debug.log('key=%s' % key)
        return hashlib.md5(key).hexdigest()


import os


def main():
    Launch('launch-detached').run()
    return


if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# End of file 
