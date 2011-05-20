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


# base class for all composite organizers
# a composite organizer organize a composite object
# it is responsible to organize the connected objects in one coherent
# presentation


class CompositeOrganizerBase(object):


    def __init__(self, drawers, orm, actor, actor_formatter):
        '''
        drawers: drawer of an object (which could be a composite)
        orm: object->db mapper
        '''
        self.drawers = drawers
        self.orm = orm
        self.actor = actor
        self.actor_formatter = actor_formatter
        return


    def __call__(self, obj):
        raise NotImplementedError


    def adjustTo(self, obj):
        key = 'customizeLubanObjectDrawer'
        if not hasattr(obj, key): return
        method = getattr(obj, key)
        method(self)
        return


    def _createMold(self):
        'create a mold to draw presentation for the object itself (no reference(set))'
        raise NotImplementedError


# version
__id__ = "$Id$"

# End of file 
