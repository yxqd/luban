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


"""script to start a cherrypy deployment.

basically this is a wrapper of cherryd, and it is used only
by <project>/deployments/cherrypy/start

see also ..stop.cherrypy
"""

def main():
    import os, optparse
    usage = "usage: %prog [options]"
    parser = optparse.OptionParser(usage, add_help_option=True)
    
    #
    parser.add_option('-p', '--port', dest='port', default=None)
    parser.add_option('-c', '--config', dest='config', default='dev.conf')

    #
    options, args = parser.parse_args()
    
    conf = options.config
    
    pidfile = os.path.abspath('cherryd.PID')
    if os.path.exists(pidfile):
        pid = open(pidfile).read()
        t = "There seems already a cherryd process running. pid=%s. \n" + \
            "If you are sure it is not running. please remove file %r"
        msg = t % (pid, pidfile)
        raise RuntimeError(msg)
    cmd = "cherryd -i cpapp -d -p %(pidfile)s -c %(conf)s" % locals()
    print("starting cherryd server ...")
    os.system(cmd)
    print('done.\n\n')

    log = os.path.abspath('site.log')
    print('*** Now start watching %s. ctrl-C to exit ***\n' % log)
    cmd = "luban tail %s" % log
    os.system(cmd)
    return


# End of file 
