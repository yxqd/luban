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


from .Property import Property
class GUID(Property):


    def __get__(self, instance, cls):
        id = super().__get__(instance, cls)
        if not id:
            from .GUID import GUID as getguid
            id = getguid(instance)
            instance.id = id
        return id


    def __set__(self, instance, value):
        if value:
            value = self._check(value)
        return super().__set__(instance, value)


    def _check(self, value):
        value = str(value)

        # verify
        # XXX is this really required?
        if value.find('.') != -1:
            raise ValueError("id cannot contain '.': %s" % value)
        
        return value



# overload this method to provide custom way of generating global
# unique id. 
def generate(obj):
    # this is really not a good implementation
    # an obviously better implementation could be using uuid
    return id(obj)



# version
__id__ = "$Id$"

# End of file 
