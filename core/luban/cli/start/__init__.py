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


import os, time, threading


def run(path, **kwds):
    if not os.path.exists(path):
        raise IOError("%r does not exist" % path)
    
    from luban.scaffolding.project import loadProject
    conf = os.path.join(path, 'conf.py')
    if not os.path.exists(conf):
        raise IOError("luban project configuration file %s does not exist" % conf)
    project = loadProject(conf)
    
    # create a deployment
    deployment = project.deployment or 'cherrypy'
    from luban.scaffolding.project.deployment import createDeployment
    deployments_path = os.path.join(path, 'deployments')
    deployment_path = createDeployment(deployment, project, deployments_path)
    # wait a bit
    time.sleep(1)
    
    # start server
    class StartServer(threading.Thread):
        def run(self):
            os.chdir(deployment_path)
            os.system('python3 start')
    StartServer().start()
    
    # XXX: need better implementation
    # wait a second and start the browser
    url = "http://localhost:8080"
    time.sleep(2)
    import webbrowser; webbrowser.open(url)
    
    return
    

def parse_cmdline():
    import optparse
    usage = "usage: %prog start [options] <project-path>"
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

