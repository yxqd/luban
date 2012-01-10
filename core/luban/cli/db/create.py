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
add a db
"""


import os, sys, time, shutil


def run(project=None):
    print ("creating db...")
    
    # load the project
    path = project or '.'
    from luban.scaffolding.project import loadProject
    project = loadProject(path)

    # change into deployment directory
    dep_path = project.getDeploymentPath()
    os.chdir(dep_path)

    # pythonpath
    project.setPythonPath()

    #
    loadModelsForWorkflows(project)

    # XXX: this is fixed to sqlalchemy for now
    from luban.db.sqlalchemy import createSession
    session = createSession()
    session.commit()
    import luban
    dburi = luban.app_config.db.uri
    print ("create db at %s. cwd: %s" % (dburi, os.path.abspath('.')))
    return


def loadModelsForWorkflows(project):
    # the project workflows subpkg
    pkgname = '%s.workflows' % project.name
    __import__(pkgname)
    pkg = sys.modules[pkgname]

    #
    from luban.workflows.models import loadModels
    loadModels(pkg)
    return


def parse_cmdline():
    import optparse
    usage = "usage: %prog db create [options]"
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

