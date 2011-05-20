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
        return


    def onProject(self, project, visual_output_type='json'):
        name = project.name
        root = Directory.Directory(name)
        root.addEntry(self._createBin(project))
        root.addEntry(self._createCgiBin(project))
        root.addEntry(self._createConfig(project))
        root.addEntry(self._createContent(project, visual_output_type=visual_output_type))
        root.addEntry(self._createHtml(project))
        root.addEntry(self._createPythonSrcTree(project))
        root.addEntry(self._createLog(project))

        subdirs = root.entries.iterkeys()
        from _mm.recurseintodirsMakemm import Generator
        generator = Generator(project.name, subdirs)
        makemm = File.File('Make.mm', generator.generate())
        root.addEntry(makemm)
        
        return root


    def _createBin(self, project):
        from _mm.datadirMakemm import Generator
        generator = Generator(project.name, 'bin', ['startservices.sh'])
        makemm = File.File('Make.mm', generator.generate())

        startservices_sh = File.File('startservices.sh', '#!/usr/bin/env sh', executable=True)
        
        bin = Directory.Directory('bin')
        bin.addEntry(makemm)
        bin.addEntry(startservices_sh)
        return bin


    def _createCgiBin(self, project):
        from _mm.datadirMakemm import Generator
        generator = Generator(project.name, 'cgi-bin', ['main.py'])
        makemm = File.File('Make.mm', generator.generate())

        from _template.main_py import content as main_py_content
        main_py = File.File('main.py', main_py_content, executable=True)
        
        cgibin = Directory.Directory('cgi-bin')
        cgibin.addEntry(makemm)
        cgibin.addEntry(main_py)
        
        return cgibin


    def _createConfig(self, project):
        files = [
            'SimpleHttpServer.pml',
            'journal.pml',
            'librarian.pml',
            'main.pml',
            'web-weaver.pml',
            ]
        config = Directory.Directory('config')

        template = 'luban.project._template'
        for f in files:

            module = '%s.%s' % (
                template, f.replace('.', '_').replace('-', '_'))
            m = __import__(module, {}, {}, [''])
            
            content = m.generate(project)

            config.addEntry(File.File(f, content))
            continue
        
        from _mm.datadirMakemm import Generator
        generator = Generator(project.name, 'config', files)
        makemm = File.File('Make.mm', generator.generate())
        config.addEntry(makemm)

        return config


    def _createHtml(self, project):
        html = Directory.Directory('html')

        html.addEntry(SymLink.SymLink('cgi-bin', '../cgi-bin'))
        html.addEntry(
            SymLink.SymLink(
                'css',
                os.path.join(common_html_base, 'css')
            ))
        html.addEntry(SymLink.SymLink('images', '../content/images'))

        js = Directory.Directory('javascripts')
        html.addEntry(js)

        js.addEntry(SymLink.SymLink(
            'jquery',
            os.path.join(common_html_base, 'javascripts', 'jquery')
            ))

        js.addEntry(SymLink.SymLink(
            'luban',
            os.path.join(common_html_base, 'javascripts', 'luban')
            ))

        js.addEntry(SymLink.SymLink(
            'other',
            os.path.join(common_html_base, 'javascripts', 'other')
            ))

        from _mm.datadirMakemm import Generator
        generator = Generator(project.name, 'html', ['.'])
        makemm = File.File('Make.mm', generator.generate())
        html.addEntry(makemm)

        return html


    def _createLog(self, project):
        log = Directory.Directory('log')

        from _mm.datadirMakemm import Generator
        generator = Generator(project.name, 'log', ['.'])
        makemm = File.File('Make.mm', generator.generate())
        log.addEntry(makemm)

        return log


    def _createPythonSrcTree(self, project):
        tree = Directory.Directory(project.name)

        from _mm.pythonpackageMakemm import Generator
        generator = Generator(project.name, ['__init__.py'])
        makemm = File.File('Make.mm', generator.generate())
        tree.addEntry(makemm)

        tree.addEntry(File.File('__init__.py', ''))
        
        return tree


    def _createContent(self, project, visual_output_type):
        contentdir = Directory.Directory('content')

        imagesdir = Directory.Directory('images')
        contentdir.addEntry(imagesdir)

        componentsdir = Directory.Directory('components')
        contentdir.addEntry(componentsdir)

        visualsdir = Directory.Directory('visuals')
        componentsdir.addEntry(visualsdir)
        
        actorsdir = Directory.Directory('actors')
        componentsdir.addEntry(actorsdir)

        visuals = project.visuals
        debug.log('visuals: %s' % visuals)
        for visual in visuals:
            name = visual.visualname
            instance = visual.visualinstance
            if not instance: continue
            s = visual2str(instance, visual_output_type)
            
            visualsdir.addEntry(
                File.File('%s.odb' % name, s)
                )
            continue

        actors = project.actors
        for actor in actors:
            name = actor.actorname
            content = actor.content

            addFileToDir(name+'.odb', content, actorsdir, create_subdir=True)
            continue
        
        return contentdir



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


def visual2str(visual, output_type):
    if isinstance(visual, basestring):
        return visual

    if output_type == 'funcs':
        from luban.weaver.UIElement2PyFuncCall import UIElement2PyFuncCall
        renderer = UIElement2PyFuncCall()
        return '\n'.join(renderer.render(visual))
    
    if output_type == 'json':
        d = visual2json(visual)
        return '''
def visual(director):
    from pyre.parsing.locators.Traceable import Traceable
    ret = Traceable()
    ret.visual_injsondict = %s
    return ret
''' % d
       


def visual2json(visual):
    from luban.weaver.Content2Dict import UIElement2Dict
    visual2json = UIElement2Dict()
    jsonRep = visual2json.render(visual)
    return jsonRep



import os

from luban._deployment import info as deployment_info
common_html_base = deployment_info.common_html_base

from luban._filesystem import Directory, File, SymLink


# version
__id__ = "$Id$"

# End of file 
