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

# This extension may conflict with other extensions. 
# If so, you may need to set the following option before using this extension.
# luban.extension_allow_override = True
"""

luban_ext_py = """
# relative path to the directory with all the static web files (js/css/images ...).
# all files in that directory will be copied into "static" directory of the deployment
static_dir = 'static' 

# extension of luban weaver web libs
# it should be a sequence of 2-tuples.
# each 2-tuple represents an extension of a library.
# each 2-tuple is in the form of
#
#   (name, extensions)
#
# where name is the name of the library to extend,
# and extensions is a dictionary describing the extension:
#
#   {'css': ...css files... ,
#    'javascripts': ...javascript modules... ,
#    'dependencies': ...dependent libraries... ,
#   }
#
weaver_web_lib_extensions = [
    # (<name of library>, <dictionary of extensions>)
    # for example
    # ('luban.core', {'css': ..., 'javascripts': ..., 'dependencies': ...})
    ]



# extension of luban widgets
# it should be a sequence of 2-tuples.
# each 2-tuple represents one widget.
# each 2-tuple is in the form of
#
#   (name, libs)
#
# where "name" is the name of the widget,
# "libs" is a list of libraries that implements this widget.
#
weaver_web_widgets_extensions = [
    # (<widget name> , <widget library names>)
    # for example
    # ('imageuploader', ['luban.widgets.imageuploader']),
    ]

"""


# version
__id__ = "$Id$"

# End of file 
