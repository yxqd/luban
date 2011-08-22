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
    director = None # the controller

    # exceptions
    from .exceptions import RoutineNotFound

    # methods
    def perform(self, routine=None, **kwds):

        if routine is None:
            routine = "default"
            
        try:
            behavior = self.__getattribute__(routine)
        except AttributeError:
            msg = "actor %s: routine '%s' is not yet implemented" % (
                self.name, routine)
            raise self.RoutineNotFound(msg)

        return behavior()
    
    pass # end of Actor


# End of file 

