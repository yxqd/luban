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
        def _(**kwds):
            return descriptors.element(default=self.getElementClass(name), **kwds)
        return _

    
    def getElementClass(self, name):
        cname = name.capitalize()
        try:
            module = __import__(cname, fromlist=['.'], globals=globals())
        except:
            import traceback
            tb = traceback.format_exc()
            msg = "Failed to get class of element %s:\n%s" % (name, tb)
            import journal
            journal.debug("ui element lookup").log(msg)
            raise KeyError(name)
        
        try:
            return getattr(module, cname)
        except:
            import traceback
            tb = traceback.format_exc()
            msg = "In looking up of element %s" % name
            msg += "Failed to get attribute %s from module %s:\n%s" % (cname, module, tb)
            import journal
            journal.debug("ui element lookup").log(msg)
            raise KeyError(name)
        
        
# version
__id__ = "$Id$"

# End of file 
