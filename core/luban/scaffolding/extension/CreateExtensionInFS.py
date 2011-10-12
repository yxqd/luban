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
renderer that create a directory tree in the file system for a luban extension
"""


# developers:
# this implementation can be improved much by separating out different
# units in the project.


class Renderer:


    def render(self, project, root='.', onconflict='skip'):
        """
        """
        tree = self.onExtension(project)
        from luban._filesystem.Writer import Writer
        writer = Writer()
        writer.render(tree, root, onconflict=onconflict)
        return
    
    
    def onExtension(self, extension):
        name = extension.name
        root = Directory.Directory(name)
        self._createPyModules(root)
        self._createWebStatic(root)
        return root


    def _createPyModules(self, root):
        root.addEntry(File.File('__init__.py', init_py))
        root.addEntry(File.File('luban_ext.py', luban_ext_py))
        return

    
    def _createWebStatic(self, root):
        static = Directory.Directory('static')
        root.addEntry(static)
        
        js = Directory.Directory('javascripts')
        static.addEntry(js)
        return


from luban._filesystem import Directory, File, SymLink


init_py = """
import luban

# This extension may have conflict with other extensions. 
# If so, you may need to set the following option before using this extension.
# luban.extension_allow_override = True
"""

luban_ext_py = """
# relative path to the directory with all the static web files (js/css/images ...).
# all files in that directory will be copied into "static" directory of the deployment
static_dir = 'static' 

# should list all js files that needs to be loaded at the start
jsfiles_toload_onstart = [
    ]
"""


# version
__id__ = "$Id$"

# End of file 
