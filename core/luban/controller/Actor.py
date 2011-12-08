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


class Actor:

    # properties
    name = None # name of the actor
    controller = None # the controller

    # exceptions
    from .exceptions import RoutineNotFound

    # methods
    def perform(self, routine=None, *args, **kwds):

        if routine is None:
            routine = "default"

        if routine.startswith('_'):
            raise RuntimeError("%s is private" % routine)
            
        try:
            behavior = self.__getattribute__(routine)
        except AttributeError:
            msg = "actor %r: routine %r is not yet implemented" % (
                self.name, routine)
            raise self.RoutineNotFound(msg)

        # special name "kwds"
        if 'kwds' in kwds:
            kwds2 = kwds['kwds']
            if isinstance(kwds2, str):
                from ..weaver.web._utils import jsonDecode
                kwds2 = jsonDecode(kwds2)
            for k in kwds2:
                if k in kwds:
                    raise RuntimeError("conflict key: %s" % k)
                continue
            kwds.update(kwds2)
            del kwds['kwds']
            
        return behavior(*args, **kwds)
    
    pass # end of Actor


# End of file 

