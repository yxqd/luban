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
# this renderer creates a project in the flavor of web.py+gae

import journal
debug = journal.debug('project2fs')


class Project2FS(object):


    def render(self, project, root='.', overwrite=False, visual_output_type='json'):
        """
        visual_output_type: if the visual is given as instance of luban elements, this option specify the output type used in the visual odb file. valid choices are 'json', 'funcs'. json: means that the output will use a json-compatible dictionary.  funcs: means that the output odb will be a few functions instantiating luban ui elements.
        """
        tree = self.onProject(project, visual_output_type=visual_output_type)
        from luban._filesystem.Writer import Writer
        writer = Writer()
        writer.render(tree, root, overwrite=overwrite)
        
        self._copyPySrcTreesToLib(os.path.join(root, tree.name))
        return


    def onProject(self, project, visual_output_type='json'):
        name = project.name
        root = Directory.Directory(name)
        root.addEntry(self._createAppYaml(project))
        root.addEntry(self._createWelcomePy(project))
        root.addEntry(self._createLib(project))
        root.addEntry(self._createStatic(project))
        return root


    def _createAppYaml(self, project):
        from templates.app_yaml import generate
        content = generate(project)
        return File.File('app.yaml', content)


    def _createWelcomePy(self, project):
        from templates.welcome_py import generate
        content = generate(project)
        return File.File('welcome.py', content)


    def _createLib(self, project):
        tree = Directory.Directory('lib')
        # json.py 
        jsonpypath = os.path.join(os.path.dirname(__file__), 'json.py')
        content = open(jsonpypath).read()
        jsonpy = File.File('json.py', content)
        tree.addEntry(jsonpy)
        return tree


    def _createStatic(self, project):
        static = Directory.Directory('static')

        static.addEntry(
            SymLink.SymLink(
                'css',
                '../lib/luban/weaver/web/css',
            ))

        static.addEntry(
            SymLink.SymLink(
                'javascripts',
                '../lib/luban/weaver/web/javascripts',
            ))

        return static


    def _copyPySrcTreesToLib(self, root):
        import luban, dsaw, journal, pyre, web
        lib = os.path.join(root, 'lib')
        copypythonsrctree(luban, lib)
        copypythonsrctree(dsaw, lib)
        copypythonsrctree(journal, lib)
        copypythonsrctree(pyre, lib)
        copypythonsrctree(web, lib)
        return


def copypythonsrctree(pkg, dest):
    pkgpath = os.path.dirname(pkg.__file__)
    pkgname = pkg.__name__
    def ignore(src, names):
        return [n for n in names if n.endswith('.pyc')]
    shutil.copytree(pkgpath, os.path.join(dest, pkgname), ignore=ignore)
    return


import os, shutil

from luban._deployment import info as deployment_info
common_html_base = deployment_info.common_html_base

from luban._filesystem import Directory, File, SymLink


# version
__id__ = "$Id$"

# End of file 
