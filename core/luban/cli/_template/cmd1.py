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


"""
sub command example
"""


import os, time


def run(project=None, **kwds):
    path = project or '.'
    if not os.path.exists(path):
        raise IOError("%r does not exist" % path)

    # load project
    from luban.scaffolding.project import loadProject
    conf = os.path.join(path, 'conf.py')
    if not os.path.exists(conf):
        raise IOError("luban project configuration file %s does not exist" % conf)
    project = loadProject(conf)

    print (project)
    return


def parse_cmdline():
    import optparse
    usage = "usage: %prog $cmd $subcmd [options]"
    parser = optparse.OptionParser(usage, add_help_option=True)
    
    # NOTE:
    # all options should have default None
    parser.add_option(
        '-p', '--project', 
        dest='project', default=None, help='path to the luban project')

    #
    options, args = parser.parse_args()
    if len(args) > 2:
        parser.error("too many arguments")

    args, kwds = [], vars(options)
    return args, kwds


# End of file 

