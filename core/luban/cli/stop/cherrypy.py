# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


"""script to stop a cherrypy deployment.

it is used only
by <project>/deployments/cherrypy/stop

see also ..start.cherrypy
"""

def main():
    import os, signal
    pidfile = os.path.abspath('cherryd.PID')
    if not os.path.exists(pidfile):
        msg = "pid file %s does not exist. process may already stopped" % pidfile
        raise RuntimeError(msg)
    pid = int(open(pidfile).read())
    print("stopping cherryd server ...")
    os.kill(pid, signal.SIGKILL)
    os.remove(pidfile)
    return


# End of file 
