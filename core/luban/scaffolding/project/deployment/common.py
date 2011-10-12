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


def populateWebStatic(root, project):
    """populate the static directory in a cherrypy deployment with 
    luban js and css files,
    and also project static files.

    root: path to the cherrypy deployment root
    project: the luban project
    """
    static = os.path.join(root, 'static')

    import luban.weaver.web
    copy_tree_from_pypkg(
        luban.weaver.web, 'javascripts', os.path.join(static, 'javascripts')
        )
    copy_tree_from_pypkg(
        luban.weaver.web, 'css', os.path.join(static, 'css')
        )

    extensions = project.extensions
    for ext in extensions:
        mod = '%s.luban_ext' % ext
        try:
            mod = __import__(mod, fromlist=[''])
        except ImportError:
            raise ImportError("failed to import %r" % mod)

        if hasattr(mod, 'static_dir'):
            # if "static_dir" is defined, use that
            copy_tree_from_pypkg(mod, mod.static_dir, static)
            
        if hasattr(mod, 'static_javascripts'):
            copy_tree_from_pypkg(
                mod, mod.static_javascripts, os.path.join(static, 'javascripts')
                )
                                 
        if hasattr(mod, 'static_css'):
            copy_tree_from_pypkg(mod, mod.static_css, os.path.join(static, 'css'))
            
        continue
        
    copy_tree(project.web_static, static)
    return


from distutils.dir_util import copy_tree
def copy_tree_from_pypkg(pkg, subdir, dest):
    """copy directory tree from a subdir of a python package
    """
    dir = os.path.dirname(pkg.__file__)
    copy_tree(os.path.join(dir, subdir), dest)
    return



# End of file 
