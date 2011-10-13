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
    
    # load project info
    from luban.scaffolding.project import loadProject
    conf = os.path.join(path, 'conf.py')
    if not os.path.exists(conf):
        raise IOError("luban project configuration file %s does not exist" % conf)
    project = loadProject(conf)
    
    # deployment
    deployment = project.deployment or 'cherrypy'
    deployment_path = os.path.join(path, 'deployments', deployment)
    
    # stop server
    os.chdir(deployment_path)
    os.system('python3 stop')

    return
    

def parse_cmdline():
    import optparse
    usage = "usage: %prog stop [options] <project-path>"
    parser = optparse.OptionParser(usage, add_help_option=True)
    
    #
    # parser.add_option(

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

