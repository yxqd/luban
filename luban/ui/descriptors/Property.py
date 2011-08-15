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


from .. import schema


STORE_NAME = '_properties'


from .Descriptor import Descriptor
class Property(Descriptor):

    type = schema.object # my type
    default = None # my default value
    

    def __get__(self, instance, cls):
        if instance is None:
            return self
        
        store = self._get_prop_store(instance)
        
        if self.name in store:
            return store[self.name]
        return self.default

    
    def __set__(self, instance, value):
        if value is None:
            # meaning to set value to "uninitialized"
            pass
        else:
            value = self.type.__cast__(value)
            
        store = self._get_prop_store(instance)
        
        store[self.name] = value
        
        return value


    def _get_prop_store(self, instance):
        if STORE_NAME not in instance.__dict__:
            setattr(instance, STORE_NAME, {})
        return getattr(instance, STORE_NAME)

            
# version
__id__ = "$Id$"

# End of file 
