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

'''
super application that wraps a pyre daemon
in addition to the configuration items in SuperApp, here we have:

 * debug: whether the daemon will be run in debug mode or not

'''


from SuperApp import SuperApp as base

class SuperAppForDaemon(base):

    class Inventory(base.Inventory):

        import pyre.inventory
        debug = pyre.inventory.bool(name='debug', default=False)
        debug.meta[base.inventory_item_signature] = True


    def runApp(self, config=None, debug=False, **kwds):

        self._info.log( 'config directories: %s' % config )

        class _(self.AppClass):


            def _configure(self):
                super(_, self)._configure()
                self._info.log('home directory: %s' % self.home)
                return


            def _getPrivateDepositoryLocations(self):
                return config


        app = _(self.appname)
        return app.run(spawn = not debug)


    def help(self):
        import sys, os
        executable = sys.argv[0]
        executable = os.path.basename(executable)
        print 'Examples'
        print '* Normal usage:' 
        print '  $ %s' % executable
        print '* Debug mode:'
        print '  $ %s -debug' % executable
        print '* Stop daemon:'
        print '  $ %s -stop' % executable
        

    def _defaults(self):
        super(SuperAppForDaemon, self)._defaults()
        
        # configurations for luban daemons  are in $EXPORT_ROOT/etc/luban-services
        if not self.inventory.config:
            import os
            from pyre.inventory.odb.prefix import _SYSTEM_ROOT
            config_dir = os.path.join(_SYSTEM_ROOT, 'luban-services')
            self.inventory.config = [config_dir]
        return


from pyre.components.Component import Component
class DaemonInterfaceToPIDStore(Component):

    class Inventory(Component.Inventory):

        import pyre.inventory
        
        from luban.components.PIDStore import PIDStore
        pidstore = pyre.inventory.facility(name='pidstore', factory=PIDStore)

        stop = pyre.inventory.bool(name='stop')
        

    def execute(self, *args, **kwds):
        stop = self.inventory.stop
        if stop:
            self._stop()
            return
        
        pid = self._loadPID()
        if pid:
            try:
                os.kill(pid, 0)
            except OSError:
                # if the daemon is not running, need to start it
                pass
            else:
                print '%s is already running. pid: %s' % (self.name, pid)
                return

        super(DaemonInterfaceToPIDStore, self).execute(*args, **kwds)
        return


    def daemon(self, pid):
        self._savePID(pid)
        super(DaemonInterfaceToPIDStore, self).daemon(pid)
        return


    def _stop(self):
        pid = self._loadPID()
        if not pid:
            print '%s: already stopped' % self.name
            return
        try:
            os.kill(pid, 9)
        except OSError:
            print '%s; tried killing pid %s and failed. already died?' % (self.name, pid)
            pass
        self._savePID(0)
        return


    def _savePID(self, pid):
        #write pid to a file
        return self.inventory.pidstore.dump(pid)


    def _loadPID(self):
        return self.inventory.pidstore.load()


    def _init(self):
        super(DaemonInterfaceToPIDStore, self)._init()
        self._init_pidstore()
        return


    def _init_pidstore(self):
        pidpath = self._pidstore_path()
        pidstore = self.inventory.pidstore
        pidstore.setPath(pidpath)
        return


    def _pidstore_path(self):
        import os
        return os.path.join(self.home, '%s.pid' % self.name)


import os


# version
__id__ = "$Id$"

# End of file 
