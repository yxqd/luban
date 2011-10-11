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

def run(path, **kwds):
    from luban.project import loadProject
    conf = os.path.join(path, 'conf.py')
    project = loadProject(conf)
    
    # XXX: should be more flexible
    deployment_path = os.path.join(project.root, 'deployments', 'cherrypy')
    # start server in a thread
    import threading
    class ServerThread(threading.Thread):

        def run(self):
            os.chdir(deployment_path)
            os.system('python start')

    ServerThread().start()

    # XXX: need better implementation
    # wait a second and start the browser
    import time; time.sleep(1)
    url = "http://localhost:8080"
    import webbrowser; webbrowser.open(url)
    
    return
    

def parse_cmdline():
    import optparse
    usage = "usage: %prog [options] start <project-path>"
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

