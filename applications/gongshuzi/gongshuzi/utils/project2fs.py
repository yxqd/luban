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


def project2fs(project, root=None, **opts):
    addDefaultActors(project, root)
    from luban.project.Project2FS import Project2FS
    renderer = Project2FS()
    return renderer.render(project, root=root, **opts)


def addDefaultActors(project, root):
    # this is not a very good implementation
    # here we need to find out if there are existing
    # actors as files (in the directory tree at "root"),
    # if they exist, we don't need to generate default actors
    # the implementation here assumes the directory tree structure
    import os
    actors_rootpath = os.path.join(root, project.name, 'content', 'components', 'actors')
    
    actors = project.actors
    actornames = [actor.actorname for actor in actors]
    
    for visual in project.visuals:
        name = visual.visualname
        if name in actornames: continue

        #
        actor_path = os.path.join(actors_rootpath, name+'.odb')
        if os.path.exists(actor_path): continue

        # create a default actor
        # if there is an actor already, skip
        if name in actornames: continue
        actor = Actor()
        actor.actorname = name
        actor.content = '''# -*- Python -*-
from luban.components.Actor import Actor as base
class Actor(base):

    
    def __init__(self, name="%s"): super(Actor, self).__init__(name)

    
    def default(self, director):
        return director.retrieveVisual("%s")

def actor(): return Actor()

        ''' % (name, name)
        
        actors.append(actor)
        continue
    return project

from luban.project.Actor import Actor

# version
__id__ = "$Id$"

# End of file 
