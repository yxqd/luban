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


class SubElementFactory:

    def __getattr__(self, key):
        from ._registry import fundamental_elements
        cls = fundamental_elements.getElementClass(key)
        
        if cls is not None \
                and self.__class__._isAllowedSubElement(cls):
            
            _ = createMethod(self, cls)
            _.__name__ = key
            return _
        
        return super().__getattr__(key)


def createMethod(container, cls):
    """create a factory method that builds a subelement of the given type
    and add it to the container
    """
    def _(**kwds):
        return createSubElement(container, cls, **kwds)
    return _

        
def createSubElement(container, cls, **kwds):
    """create a sub elment of given type, and add it to the container
    """
    e = cls(**kwds)
    # give it a name if necessary
    if not e.name:
        e.name = "e{!s}".format(len(container.contents))
            
    container.append(e)
    return e


# End of file 
