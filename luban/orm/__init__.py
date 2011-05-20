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


def orm(db, guid, **kwds):
    # db: db manager
    # guid: guid generator
    from dsaw.model.visitors.OrmManager import OrmManager
    return OrmManager(db, guid, **kwds)


def viewFactory(**kwds):
    from views.View import Factory
    return Factory(**kwds)


def object2formfields(orm, **kwds):
    from Object2FormFields import Object2FormFields
    return Object2FormFields(orm, **kwds)


def object2form(orm, **kwds):
    o2ff = object2formfields(orm, **kwds)
    from Object2Form import Object2Form
    return Object2Form(o2ff)


def object2actor(kls, needauthorization=True, **kwds):
    if needauthorization:
        from luban.components.AuthorizedActor import AuthorizedActor as base
    else:
        from luban.components.Actor import Actor as base
    if kwds.has_key('ActorBase'):
        base = kwds['ActorBase']
        del kwds['ActorBase']
        
    from Object2Actor import object2actor
    Actor = object2actor(kls, ActorBase=base, **kwds)
    return Actor
    

def abstractbase2actor(base, subclasses,  **kwds):
    from AbstractBase2Actor import abstractbase2actor
    return abstractbase2actor(base, subclasses, **kwds)
    

# version
__id__ = "$Id$"

# End of file 
