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
        # key is the factory name of the subelement
        from ._registry import element_types
        subelemtype = element_types.getElementClass(key)
        
        if subelemtype is not None \
                and self.__class__._isAContainerOf(subelemtype):
            
            _ = createMethod(self, subelemtype)
            _.__name__ = key
            # ctor_name = self.__class__.__unique_type_name__ + '.' + key
            ctor_name = key
            _.__doc__ = subelemtype.getCtorDocStr(ctor_name = ctor_name)
            from .decorators import elementfactory
            return elementfactory(_)
        
        raise AttributeError(key)


def createMethod(container, subelem):
    """create a factory method that builds a subelement of the given type
    and add it to the container
    """
    def _(**kwds):
        return createSubElement(container, subelem, **kwds)
    return _

        
def createSubElement(container, subelem, **kwds):
    """create a sub elment of given type, and add it to the container
    """
    e = subelem(**kwds)
    # give it a name if necessary
    if not e.name:
        e.name = "e{!s}".format(len(container.contents))
            
    container.append(e)
    return e


# End of file 
