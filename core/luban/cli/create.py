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
    from ..scaffolding.project import createProjectSkeleton
    createProjectSkeleton(name, outdir)
    return
    

def parse_cmdline():
    import optparse
    usage = "usage: %prog [options] create project-name"
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
        parser.error("project name must be specified. for more help:\n\n  $ luban create -h\n\n")
    args, kwds = args[1:], vars(options)
    return args, kwds

# End of file 

