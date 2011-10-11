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

start = """
#!/usr/bin/env python

import sys, os

if len(sys.argv) == 2 and sys.argv[1] == 'production':
    conf = 'prod.conf'
else:
    conf = 'dev.conf'

cmd = "cherryd -i cpapp -c %s" % conf
os.system(cmd)

"""



def createCpApp(project):
    root = Directory.Directory('cpapp')
    init = File.File('__init__.py', cpapp_init % project.__dict__)
    root.addEntry(init)
    return root

cpapp_init = """# -*- python -*-

project_pytree_container = %(pytree_container)r
import sys
if project_pytree_container not in sys.path:
    sys.path.insert(0, project_pytree_container)

import os.path
current_dir = os.path.dirname(os.path.abspath(__file__))

# luban.timber
from luban.timber.controller.CherrypyController import CherrypyController
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




def populateWebStatic(root, project):
    """populate the static directory in a cherrypy deployment with 
    luban js and css files,
    and also project static files.

    root: path to the cherrypy deployment root
    project: the luban project
    """
    import os
    static = os.path.join(root, 'static')

    import luban.weaver.web
    copy_static_from_luban_web_weaver_pkg(luban.weaver.web, static)

    import luban.timber.weaver.web
    copy_static_from_luban_web_weaver_pkg(luban.timber.weaver.web, static)

    copy_tree(project.web_static, static)
    return


from distutils.dir_util import copy_tree
import os
def copy_static_from_luban_web_weaver_pkg(pkg, dest):
    dir = os.path.dirname(pkg.__file__)
    copy_tree(os.path.join(dir, 'javascripts'), os.path.join(dest, 'javascripts'))
    copy_tree(os.path.join(dir, 'css'), os.path.join(dest, 'css'))
    return



# End of file 
