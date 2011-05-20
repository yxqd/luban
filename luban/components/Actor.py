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


class RoutineNotFound(Exception): pass


from pyre.components.Component import Component

class Actor(Component):


    class Inventory(Component.Inventory):

        import pyre.inventory
        
        # the code of the key that user press
        keycode = pyre.inventory.str('keycode')
        
        
        
    def perform(self, director, routine=None, debug=False):
        """construct an actual page by invoking the requested routine"""
        
        if routine is None:
            routine = "default"
            
        try:
            behavior = self.__getattribute__(routine)
        except AttributeError:
            raise RoutineNotFound, "actor %s: routine '%s' is not yet implemented" % (
                self.name, routine)

        return behavior(director)


    def __init__(self, name):
        super(Actor, self).__init__(name, facility='actor')
        self.routine = None
        return



# inherit from this class in addition to the Actor class will make the actor
# capable of accepting any inputs in the inventory without the need to
# explicitly declare the input
class AcceptArbitraryInput:


    def updateConfiguration(self, registry):
        listing = self._listing(registry)
        if listing:
            for k, v in listing:
                setattr(self.inventory, k, v)        
        return []

    
    def _listing(self, registry):
        if not registry: return []
        listing = [
            (name, descriptor.value) for name, descriptor in registry.properties.iteritems()
            ]

        listing += [
            ("%s.%s" % (nodename, name), value)
            for nodename, node in registry.facilities.iteritems()
            for name, value in self._listing(node)
            ]

        return listing


class Receptionist(AcceptArbitraryInput, Actor):

    pass 


# version
__id__ = "$Id$"

# End of file 
