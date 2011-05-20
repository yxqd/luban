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


"""
establish ssh tunnel.

The tunnel will be running on the background and the script
will instantly return.

The script save files in a directory specified by the "home"
property (defaults to /tmp):

 <sig>.pid: process id of the tunnel
 <sig>.info: information about the tunnel

If the tunnel is already established and this command is rerun
with the same parameter, no new tunnel-establishment will be
run.

"""


#from pyre.applications.Daemon import Daemon as Stager
from pyre.applications.Application import Application
from pyre.applications.Script import Script

class SSHTunnel(Script): #, Stager):

    class Inventory(Script.Inventory):

        import pyre.inventory
        home = pyre.inventory.str('home', default = '/tmp')
        
        remote = pyre.inventory.str('remote', default = 'remote.host:22')
        localport = pyre.inventory.int('localport', default = 0)
        through = pyre.inventory.str('through', default = '')
        
        from luban.components.PIDStore import PIDStore
        pidstore = pyre.inventory.facility(name='pidstore', factory=PIDStore)


    def main(self, *args, **kwds):
        cmd = self._getCmd()
        self._setPIDpath(cmd)
        
        pid = self._loadPID()
        if pid:
            import os
            try:
                os.kill(pid, 0)
            except OSError:
                # if the daemon is not running, need to start it
                pass
            else:
                print '%s is already running. pid: %s' % (cmd, pid)
                return

        self.connect(*args, **kwds)
        return


    def connect(self, *args, **kwds):
        cmd = self._getCmd()

        import subprocess, shlex
        args = shlex.split(cmd)

        import os
        home = self.home
        if not os.path.exists(home):
            os.makedirs(home)
        self._saveCmd(cmd)

        null = open('/dev/null', 'r')
        log = os.path.join(home, '%s.log' % cmd)
        stream = open(log, 'w')
        
        p = subprocess.Popen(args, stdin=null, stdout=stream, stderr=stream)
        pid = p.pid

        import time
        time.sleep(1)

        r = p.poll()
        if r:
            stream.close()
            out = open(log).read()
            print "Command\n\n  %s\n\nfailed. \nOutput from the command:\n\n%s" % (cmd, out)
        else:
            print "Command\n\n  %s\n\nis running. \npid: %s" % (cmd, pid)
            self._savePID(pid)
        return


    def _configure(self):
        super(SSHTunnel, self)._configure()
        self.home = self.inventory.home

        remote = self.inventory.remote
        host, port = remote.split(':')
        self.rhost = host
        self.rport = port

        self.lport = self.inventory.localport
        # through defaults to remote host
        through = self.inventory.through or host
        splits = through.split(':')
        if len(splits) == 2:
            self.thruhost, self.thruport = splits
        else:
            self.thruhost = through
            self.thruport = 22
        return


    def _getCmd(self):
        cmd = 'ssh -t -t -L %s:%s:%s -p %s %s' % (
            self.lport, self.rhost, self.rport, self.thruport, self.thruhost)
        return cmd


    def _saveCmd(self, cmd):
        p = os.path.join(self.home, '%s.info' % self._signatue())
        s = open(p, 'w')
        s.write('home=%s\n' % self.inventory.home)
        s.write('remote=%s\n' % self.inventory.remote)
        s.write('localport=%s\n' % self.inventory.localport)
        s.write('through=%s\n' % self.inventory.through)
        s.write('cmd=%s\n' % cmd)
        return


    def _savePID(self, pid):
        #write pid to a file
        return self.inventory.pidstore.dump(pid)


    def _loadPID(self):
        return self.inventory.pidstore.load()


    def _setPIDpath(self, cmd):
        pidpath = os.path.join(self.home, '%s.pid' % self._signatue())

        pidstore = self.inventory.pidstore
        pidstore.setPath(pidpath)
        return

    
    def _signatue(self):
        k = '%s-%s' % (self._getCmd(), self.home)
        import hashlib
        h = hashlib.md5(k).hexdigest()
        return 'sshtunnel-%s' % h


import os

def main():
    SSHTunnel('sshtunnel').run()
    return


# version
__id__ = "$Id$"

# End of file 
