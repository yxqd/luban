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


from .DynamicProperty import DynamicProperty as base
class ID(base):
    """
    special property for id

    need to make sure if id is already set, not more setting 
    is allowed
    """

    def __init__(self, **kwds):
        super().__init__(**kwds)
        from .. import schema
        self.type = schema.str
        return
    
    
    def __set__(self, instance, value):
        old = self.__get__(instance, instance.__class__)
        if old is not None:
            m = "id for element %s is already set to %s" % (
                instance, old)
            raise ValueError(m)
        return super().__set__(instance, value)


# End of file 
