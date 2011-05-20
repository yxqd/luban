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


def initorm():
    from orm import ORM
    orm = ORM()

    from uielements import getElementClasses
    klasses = getElementClasses()

    for kls in klasses:
        orm.registerObject(kls)
        continue

    from luban.project.Project import Project as ProjectObject
    from Session import Project as ProjectTable
    orm.registerObject(ProjectObject, Table=ProjectTable)

    from luban.project.Visual import Visual
    from luban.project.Actor import Actor
    for t in [Visual, Actor]:
        orm.registerObject(t)

    return orm


def tables():
    '''tables that are not created from orm'''
    from Session import Session
    from ProjectSettings import ProjectSettings
    ret = [
        Session,
        ProjectSettings,
        ]
    return ret


# version
__id__ = "$Id$"

# End of file 
