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

from luban import py_major_ver


from .Property import Property
class DynamicProperty(Property):
    """
    special property that could be assigned different types

    for example, a property could usually be a string type, but it could
    be assigned with an action that when evaluated, returns a string type.
    """
    
    def __set__(self, instance, value):
        
        # if value is an action, it is ok
        from ..actions.ActionBase import ActionBase
        if isinstance(value, ActionBase):
            store = self._get_prop_store(instance)
            store[self.name] = value
            return value

        if py_major_ver == 2:
            return super(DynamicProperty, self).__set__(instance, value)
        else:
            return super().__set__(instance, value)


# End of file 
