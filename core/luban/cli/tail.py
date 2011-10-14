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


import os, time


def run(path, **kwds):
    if not os.path.exists(path):
        raise IOError("%r does not exist" % path)

    # handle ctrl-c
    def onsigint(signal, frame):
        print ('\nexiting from "tailing" %s ...' % path)
        import sys; sys.exit()
        return
    import signal
    signal.signal(signal.SIGINT, onsigint)
    
    from luban.utils.tail import tail
    tail(path, **kwds)
    return
    

def parse_cmdline():
    import optparse
    usage = "usage: %prog tail [options] filename"
    parser = optparse.OptionParser(usage, add_help_option=True)
    
    #
    # parser.add_option(

    #
    options, args = parser.parse_args()
    if len(args) != 2:
        parser.error("too few arguments. must give filename")
        
    path = args[1]

    args, kwds = [path], vars(options)
    return args, kwds

# End of file 

