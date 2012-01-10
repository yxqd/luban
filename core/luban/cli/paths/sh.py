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
env vars for sh
"""


import os, sys, time, shutil


def run(project=None):
    path = project or '.'
    from luban.scaffolding.project import loadProject
    project = loadProject(path)
    
    pytreeroot = project.getPyTreeRoot()
    s = []
    s.append('export PYTHONPATH="%s":${PYTHONPATH}' % pytreeroot)
    print ('\n'.join(s))
    return 


def parse_cmdline():
    import optparse
    usage = "usage: %prog paths sh [options]"
    parser = optparse.OptionParser(usage, add_help_option=True)
    
    # NOTE:
    # all options should have default None
    parser.add_option(
        '-p', '--project', 
        dest='project', default=None, help='path to the luban project')

    #
    options, args = parser.parse_args()
    if len(args) != 2:
        msg = "incorrect number of arguments.\n\n"
        parser.error(msg)

    args, kwds = [], vars(options)
    return args, kwds


# End of file 

