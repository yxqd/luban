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
This is a overarching script to start a luban project

the starting process really depends on the deployment mechanism.

so the options for the start script need to be passed
to the underlying starting script for the particular deployment.

at this moment only option is "port", the port number.
"""


# command line options 
server_options = [
    'port',
    ]
options = server_options


import os, time, threading


def run(path, **kwds):
    if not os.path.exists(path):
        raise IOError("%r does not exist" % path)

    # sanity check
    for k in kwds:
        assert k in options
        continue
    
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
    # wait a bit
    time.sleep(1)
    
    # start server
    class StartServer(threading.Thread):
        def run(self):
            os.chdir(deployment_path)
            optstr = ' '.join('--%s=%s' % (k, getattr(project, k)) for k in server_options)
            os.system('python3 start %s' % optstr)
    StartServer().start()
    
    # XXX: need better implementation
    # wait a second and start the browser
    port = project.port
    url = "http://localhost:%s" % port
    time.sleep(2)
    import webbrowser; webbrowser.open(url)
    
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
    usage = "usage: %prog start [options] <project-path>"
    parser = optparse.OptionParser(usage, add_help_option=True)
    
    # NOTE:
    # all options should have default None
    parser.add_option('-p', '--port', dest='port', default=None)

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

