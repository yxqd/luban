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


from pyre.applications.Application import Application
from pyre.applications.Daemon import Daemon as Stager
from pyre.applications.ComponentHarness import ComponentHarness

class SimpleHttpServerDaemon(Application, Stager, ComponentHarness):

    class Inventory(Application.Inventory):
        
        import pyre.inventory
        
        home = pyre.inventory.str('home', default='/tmp')

        stdin = pyre.inventory.str('stdin', default='/dev/null')
        stdout = pyre.inventory.str('stdout', default='/dev/null')
        stderr = pyre.inventory.str('stderr', default='stdout')


    def execute(self, *args, **kwds):
        kwds['stdin'] = self.inventory.stdin
        stdout = kwds['stdout'] = self.inventory.stdout
        stderr = self.inventory.stderr
        if stderr == 'stdout':
            stderr = stdout
        kwds['stderr'] = stderr
        
        super(SimpleHttpServerDaemon, self).execute(*args, **kwds)
        return
        
        
    def main(self, *args, **kwds):
        try:
            component = self.harnessComponent()
            if not component:
                return
        
            component.serve()
        except:
            import traceback
            tb = traceback.format_exc()
            open('/tmp/e.log', 'w').write(tb)
        return


    def createComponent(self):
        return Server()


    def _configure(self):
        super(SimpleHttpServerDaemon, self)._configure()
        import os
        self.home = os.path.abspath(self.inventory.home)
        return


from pyre.components.Component import Component
class Server(Component):


    class Inventory(Component.Inventory):
        
        import pyre.inventory
        
        port = pyre.inventory.int('port', default=8080)
        

    def serve(self):
        # print self.name
        port = self.inventory.port
        import SocketServer
        from SimpleHttpServer import ScriptRequestHandler
        
        s=SocketServer.TCPServer(('',port),ScriptRequestHandler)
        msg = "ScriptServer running on port %s" %port 
        self._info.log( msg )
        # print msg

        s.serve_forever()
        return


    def __init__(self):
        super(Server, self).__init__('SimpleHttpServer', 'server')
        return
    

# version
__id__ = "$Id$"

# End of file 
