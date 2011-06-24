# -*- python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# mapping name to facility factory of ui elements
class UIElementFacilityMapping:

    def __init__(self, elements=None):
        self.elements = elements
        return


    def __getitem__(self, key):
        if self.elements == 'all' or key in self.elements:
            return self.getElementFacilityFactory(key)
        raise KeyError(key)


    def getElementFacilityFactory(self, name):
        from .. import descriptors 
        return descriptors.element(default=self.getElementClass(name))

    
    def getElementClass(self, name):
        cname = name.capitalize()
        module = __import__(cname, fromlist=['.'], globals=globals())
        return getattr(module, cname)
        
        
# version
__id__ = "$Id$"

# End of file 
