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


from pyre.components.Component import Component

class Actor(Component):


    def perform(self, director, routine=None, debug=False):
        msg = ("This actor is not implemented.\n"
               "When you see this message, it usually means that the actor you "
               "try to use is not implemented and it results in fallback to "
               "this default actor."
               "director: %s, routine: %s, debug: %s" % (director, routine, debug)
               )
        raise NotImplementedError, msg


    def __init__(self, name='notimplemented'):
        super(Actor, self).__init__(name, facility='actor')
        return


# version
__id__ = "$Id$"

# End of file 
