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


from .DynamicProperty import DynamicProperty as base
class ID(base):
    """
    special property for id

    need to make sure if id is already set, not more setting 
    is allowed
    """

    def __init__(self, **kwds):
        if py_major_ver == 2:
            super(ID, self).__init__(**kwds)
        elif py_major_ver == 3:
            super().__init__(**kwds)
            
        from .. import schema
        self.type = schema.str
        return
    
    
    def __set__(self, instance, value):
        # we don't automatically asign a unique id
        # we only check if the id is valid
        # it could be None, or a good string
        old = self.__get__(instance, instance.__class__)
        if old is not None:
            m = "id for element %s is already set to %s" % (
                instance, old)
            raise ValueError(m)
        
        if py_major_ver == 2:
            superme = super(ID, self)
        elif py_major_ver == 3:
            superme = super()

        if value is None:
            return superme.__set__(instance, value)
            
        if not isinstance(value, str):
            value = str(value)
            
        if bad_id(value):
            raise ValueError("not a valid id: %s" % value)
        
        return superme.__set__(instance, value)



# no space, no special characters, only alphanumeric characters
import re
pattern = re.compile('[^a-zA-Z0-9_-]')
def bad_id(id):
    return bool(pattern.search(id))


# End of file 
