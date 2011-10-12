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


import os

def run(name, outdir = None, **kwds):
    outdir = outdir or '.'
    from ..scaffolding.extension import createExtensionSkeleton
    createExtensionSkeleton(name, outdir)
    print('extension %r created' % name)
    return
    

def parse_cmdline():
    print ("luban creatext: create a luban extension\n")
    import optparse
    usage = "usage: %prog createext [options] extension-name"
    parser = optparse.OptionParser(usage, add_help_option=True)
    
    #
    parser.add_option(
        '-o', '--outdir', 
        dest='outdir', 
        help='output directory. default: .', 
        default='.',
        )

    #
    options, args = parser.parse_args()
    if len(args) < 2:
        parser.error("extension name must be specified. for more help:\n\n  $ luban createext -h\n\n")
    args, kwds = args[1:], vars(options)
    return args, kwds

# End of file 

