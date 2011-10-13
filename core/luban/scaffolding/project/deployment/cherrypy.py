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


from luban._filesystem import Directory, File, SymLink

def createTree(project):
    """create a directory tree for cherrypy deployment for a luban project
    """
    root = Directory.Directory('cherrypy')
    
    root.addEntry(File.File('dev.conf', dev_conf))
    root.addEntry(File.File('prod.conf', prod_conf))
    
    root.addEntry(File.File('start', start, executable=1))
    root.addEntry(File.File('stop', stop, executable=1))

    root.addEntry(createCpApp(project))

    root.addEntry(Directory.Directory('static'))
    
    return root


dev_conf = """
[global]
server.socket_host: '0.0.0.0'
server.socket_port: 8080
engine.autoreload_on: True
log.error_file: 'site.log'
log.screen: True

tree.cpapp: cherrypy.Application(cpapp.Root())


[/]
tools.staticdir.root: cpapp.current_dir + "/.."

[/static]
tools.staticdir.on: True
tools.staticdir.dir: "static"

"""

prod_conf = """
[global]
environment: 'production'
log.error_file: 'site.log'
log.screen: True

tree.cpapp: cherrypy.Application(cpapp.Root())


[/]
tools.staticdir.root: cpapp.current_dir + "/.."

[/static]
tools.staticdir.on: True
tools.staticdir.dir: "static"

"""

start = """#!/usr/bin/env python

import sys, os

if len(sys.argv) == 2 and sys.argv[1] == 'production':
    conf = 'prod.conf'
else:
    conf = 'dev.conf'

pidfile = os.path.abspath('cherryd.PID')
if os.path.exists(pidfile):
    pid = open(pidfile).read()
    t = "There seems already a cherryd process running. pid=%s. \\n" + \\
        "If you are sure it is not running. please remove file %r"
    msg = t % (pid, pidfile)
    raise RuntimeError(msg)
cmd = "cherryd -i cpapp -d -p %(pidfile)s -c %(conf)s" % locals()
print("starting cherryd server ...")
os.system(cmd)
print('done.\n\n')
"""

stop = """#!/usr/bin/env python

import os, signal
pidfile = os.path.abspath('cherryd.PID')
if not os.path.exists(pidfile):
    msg = "pid file %s does not exist. process may already stopped" % pidfile
    raise RuntimeError(msg)
pid = int(open(pidfile).read())
print("stopping cherryd server ...")
os.kill(pid, signal.SIGKILL)
os.remove(pidfile)
"""

def createCpApp(project):
    root = Directory.Directory('cpapp')
    init = File.File('__init__.py', cpapp_init % project.__dict__)
    root.addEntry(init)
    return root

cpapp_init = """# -*- python -*-

# make sure project python package is in path
project_pytree_container = %(pytree_container)r
import sys
if project_pytree_container not in sys.path:
    sys.path.insert(0, project_pytree_container)

# make sure to load all luban extenssions
import luban
luban.load_extensions(%(extensions)s)

# this is to let cherrypy where the application is
import os.path
current_dir = os.path.dirname(os.path.abspath(__file__))

# controller
from luban.controller.CherrypyController import CherrypyController
class Root(CherrypyController):

    def __init__(self):
        super().__init__(
            url = '/',
            static_html_base = 'static',
            actor_packages = [%(actors_pkg)r],
            stylesheets = ['%(name)s.css'],
            )
        return

"""



from .common import populateWebStatic


# End of file 
