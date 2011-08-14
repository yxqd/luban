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

    def __getattribute__(self, key):
        from ._registry import fundamental_elements
        cls = fundamental_elements.getElementClass(key)
        
        if cls is not None \
                and self.__class__._isAllowedSubElement(cls):
            
            def _(**kwds):
                e = cls(**kwds)
                self.append(e)
                return e
            _.__name__ = key
            return _
        
        return super().__getattribute__(key)


# End of file 
