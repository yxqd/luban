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
This is a overarching script to deploy a luban project
"""


import os, time, threading


def run(path, **kwds):
    if not os.path.exists(path):
        raise IOError("%r does not exist" % path)

    # load project
    from luban.scaffolding.project import loadProject
    conf = os.path.join(path, 'conf.py')
    if not os.path.exists(conf):
        raise IOError("luban project configuration file %s does not exist" % conf)
    project = loadProject(conf)

    # update project if necessary
    updateProjectConfiguration(project, **kwds)

    # create a deployment
    deployment = project.deployment or 'cherrypy'
    from luban.scaffolding.project.deployment import createDeployment
    deployments_path = os.path.join(path, 'deployments')
    deployment_path = createDeployment(deployment, project, deployments_path)
    
    return


def updateProjectConfiguration(project, **kwds):
    # port
    port = kwds.get('port')
    if port:
        project.port = port
        
    writeProjectConfiguration(project)
    return


def writeProjectConfiguration(project):
    from ...scaffolding.project.ConfigurationWriter import ConfigurationWriter
    writer = ConfigurationWriter()
    writer.dump(project)
    return
    

def parse_cmdline():
    import optparse
    usage = "usage: %prog deploy [options] <project-path>"
    parser = optparse.OptionParser(usage, add_help_option=True)
    
    # NOTE:
    # all options should have default None
    # parser.add_option('-p', '--port', dest='port', default=None)

    #
    options, args = parser.parse_args()
    if len(args) > 2:
        parser.error("too many arguments")
    elif len(args) == 2:
        path = args[1]
    else:
        path = '.'

    args, kwds = [path], vars(options)
    return args, kwds

# End of file 

