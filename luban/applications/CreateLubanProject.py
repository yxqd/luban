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


from ProjectScriptBase import ProjectScriptBase as base

class CreateLubanProject(base):

    class Inventory(base.Inventory):

        import pyre.inventory
        overwrite = pyre.inventory.bool('overwrite', default=False)

        outdir = pyre.inventory.str('outdir', default='.')

        flavor = pyre.inventory.str('flavor', default='')
        
        
    def main(self):
        name = self.project
        self._checkProjectName(name)

        from luban.project.Project import Project
        project = Project()
        project.name = name

        # create a visual
        visual = self._createVisual(project)
        # add it to the project
        project.visuals.append(visual)

        # create a actor
        actor = self._createActor(project)
        # add it to the project
        project.actors.append(actor)

        # create project
        flavor = self.inventory.flavor
        if flavor:
            modname = 'luban.project._types.%s.Project2FS' % flavor
            mod = __import__(modname, {}, {}, [''])
            Project2FS = getattr(mod, 'Project2FS')
        else:
            from luban.project.Project2FS import Project2FS
            
        outdir = self.inventory.outdir
        overwrite = self.inventory.overwrite
        renderer = Project2FS()
        renderer.render(project, outdir, overwrite=overwrite)
        
        return


    def _defaults(self):
        super(CreateLubanProject, self)._defaults()
        self.inventory.project = 'helloworld'
        return


    def _checkProjectName(self, name):
        import re
        p = re.compile('[^0-9a-zA-Z_]')
        m = p.search(name)
        if m:
            raise ValueError, "Project name %r contains invalid character %r" % (
                name, m.group())

        p = re.compile('^[^a-zA-Z_]')
        m = p.search(name)
        if m:
            raise ValueError, "Project name %r starts with invalid character %r" % (
                name, m.group())
        
        return name


    def _createVisual(self, project):
        code = """
def visual(director):
    import luban.content
    frame = luban.content.frame(title='test frame')
    
    doc = frame.document(title='Hello world!')
    doc.paragraph().text = ['This is a test frame.']
    
    return frame
"""
        from luban.project.Visual import Visual
        visual = Visual()
        visual.visualname=project.name
        visual.visualinstance = code
        
        return visual


    def _createActor(self, project):
        class _:
            actorname = project.name
            content = """
def actor():
    from luban.components.Actor import Actor as base
    class Actor(base):
        def default(self, director):
            return director.retrieveVisual('%s')
    return Actor('%s')
""" % (project.name, project.name)
        return _

        
# version
__id__ = "$Id$"

# End of file 
