# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


"""
renderer that create a directory tree in the file system for a luban project
"""


# developers:
# this implementation can be improved much by separating out different
# units in the project.


class Renderer:


    def render(self, project, root='.', overwrite=False):
        """
        """
        tree = self.onProject(project)
        from luban._filesystem.Writer import Writer
        writer = Writer()
        writer.render(tree, root, overwrite=overwrite)
        return
    
    
    def onProject(self, project):
        name = project.name
        root = Directory.Directory(name)
        root.addEntry(self._createPythonPackage(project))
        root.addEntry(self._createWebDir(project))
        root.addEntry(self._createConfFile(project))
        return root


    def _createConfFile(self, project):
        fn = "proj.conf"
        from .templates import proj_conf
        content = proj_conf.create(project)
        return File.File(fn, content)
    
    
    def _createPythonPackage(self, project):
        # the python package for the project 
        name = project.name
        root = Directory.Directory(project.pytree_container)

        # it must at least has a sub package for luban actors
        tree = makePyTreeWithSubPkg(project.actors_pkg)
        root.addEntry(tree)
        
        return root
    
    
    def _createWebDir(self, project):
        web_static = project.web_static
        tokens = web_static.split('/')
        name = tokens[0]
        root = Directory.Directory(name)
        addFileToDir('/'.join(tokens[1:]) + '/index.html', '', root)
        return root


def makePyTreeWithSubPkg(subpkg):
    """create the hierarchy of directories and files to establish
    the given python sub packages. 
    for example, subpkg = "a.b.c"
    dir(a)
    + __init__.py
    + dir(b)
      + __init__.py
      + dir(c)
        + __init__.py
    """
    tokens = subpkg.split('.')
    parent = root = Directory.Directory(tokens[0])
    parent.addEntry(File.File('__init__.py', ''))
    for token in tokens[1:]:
        dir = Directory.Directory(token)
        parent.addEntry(dir)
        dir.addEntry(File.File('__init__.py', ''))
        parent = dir
        continue
    return root

    
    
def addFileToDir(path, content, dir, create_subdir=True):
    if not path: raise RuntimeError
    splits = path.split('/')
    if len(splits) > 1 and create_subdir==False:
        raise RuntimeError

    for subdir in splits[:-1]:
        subdir = Directory.Directory(subdir)
        dir.addEntry(subdir)
        dir = subdir
        continue

    dir.addEntry(File.File(splits[-1], content))
    return


from luban._filesystem import Directory, File, SymLink


# version
__id__ = "$Id$"

# End of file 
