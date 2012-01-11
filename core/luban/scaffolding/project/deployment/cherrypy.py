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

    root.addEntry(createAppConfigPy(project))
    
    root.addEntry(File.File('dev.conf', dev_conf))
    root.addEntry(File.File('prod.conf', prod_conf))
    
    root.addEntry(File.File('start', start, executable=1))
    root.addEntry(File.File('stop', stop, executable=1))

    root.addEntry(createCpApp(project))

    root.addEntry(Directory.Directory('static'))
    
    return root


def createAppConfigPy(project):
    import luban
    luban.load_extensions(project.extensions)
    options = luban.app_config.options
    s = ''
    for opt in options.values():
        s += opt.example_code()
        continue
    return File.File('luban_app_config.py', s)


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
tools.sessions.on: True
# tools.sessions.storage_type: "file"
# tools.sessions.storage_path: "data/sessions"
tools.sessions.timeout: 60

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
from luban.cli.start.cherrypy import main
main()
"""

stop = """#!/usr/bin/env python
from luban.cli.stop.cherrypy import main
main()
"""

def createCpApp(project):
    root = Directory.Directory('cpapp')
    init = File.File('__init__.py', cpapp_init % project.__dict__)
    root.addEntry(init)
    return root

cpapp_init = """# -*- python -*-

# load project info
from luban.scaffolding.project import loadProject
project = loadProject('../..') # assume the cwd is <deployment> directory

# make sure project python package is in path
project_pytree_container = project.pytree_container
import sys
if project_pytree_container not in sys.path:
    sys.path.insert(0, project_pytree_container)

# make sure to load all luban extensions
import luban
luban.load_extensions(project.extensions)

# this is to let cherrypy where the application is
import os.path
current_dir = os.path.dirname(os.path.abspath(__file__))

# controller
from luban.controller.CherrypyController import CherrypyController
class Root(CherrypyController):

    def __init__(self):
        from luban import py_major_ver
        if py_major_ver == 2:
            superme = super(Root, self)
        elif py_major_ver == 3:
            superme = super()
        superme.__init__(
            url = '/',
            static_html_base = '/static',
            actor_packages = [project.actors_pkg],
            stylesheets = ['%(name)s.css'],
            )
        return

"""



from .common import populateWebStatic


# End of file 
