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



# renderer that create a directory tree in the file system for a luban project


class Project2FS(object):


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
        return root


    def _createPythonPackage(self, project):
        name = project.name
        root = Directory.Directory('python')
        addFileToDir('__init__.py', '', root)
        
        actors = Directory.Directory('actors')
        root.addEntry(actors)

        addFileToDir('__init__.py', '', actors)
        
        return root


    def _createWebDir(self, project):
        root = Directory.Directory('web')
        
        static = Directory.Directory('static')
        root.addEntry(static)
        
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
