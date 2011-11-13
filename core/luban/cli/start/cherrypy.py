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
    
    # make sure cherryd is not yet started
    pidfile = os.path.abspath('cherryd.PID')
    if os.path.exists(pidfile):
        pid = open(pidfile).read()
        t = "There seems already a cherryd process running. pid=%s. \n" + \
            "If you are sure it is not running. please remove file %r"
        msg = t % (pid, pidfile)
        raise RuntimeError(msg)

    # the configuration file
    conf = options.config

    # fix port
    port = options.port
    modifyConfigration(conf, port=port)
    
    # start 
    cmd = "cherryd -i cpapp -p %(pidfile)s -c %(conf)s" % locals()
    print("starting cherryd server ...")
    os.system(cmd)
    print('done.\n\n')

    # log = os.path.abspath('site.log')
    # print('*** Now start watching %s. ctrl-C to exit ***\n' % log)
    # cmd = "luban tail %s" % log
    # os.system(cmd)
    return


def modifyConfigration(conf, **kwds):
    newconf = createNewConfig(conf, **kwds)
    import os
    os.remove(conf)
    os.rename(newconf, conf)
    return


def createNewConfig(conf, port=None):
    # parser
    from configparser import SafeConfigParser as ConfigParser
    cp = ConfigParser()
    cp.optionxform = str

    # read 
    read = cp.read(conf)
    assert conf in read

    # port
    if port:
        cp.set('global', 'server.socket_port', port)

    newconf = conf + '.new'
    cp.write(open(newconf, 'w'))
    return newconf


# End of file 
