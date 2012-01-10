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
add a workflow
"""


import os, time


def run(workflow, project=None):
    project = project or '.'
    project = os.path.abspath(project)
    print ("adding workflow %r to luban project %r" % (workflow, project))
    return


def parse_cmdline():
    import optparse
    usage = "usage: %prog workflows add <workflow> [options]"
    parser = optparse.OptionParser(usage, add_help_option=True)
    
    # NOTE:
    # all options should have default None
    parser.add_option(
        '-p', '--project', 
        dest='project', default=None, help='path to the luban project')

    #
    options, args = parser.parse_args()
    if len(args) != 3:
        parser.error("incorrect number of arguments")

    args, kwds = args[2:], vars(options)
    return args, kwds


# End of file 

