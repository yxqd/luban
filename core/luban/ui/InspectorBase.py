# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


basic_types = int, str, bool

class InspectorBase:

    def onAny(self, value):
        "generic handler"
        if value is None:
            return
        
        for t in basic_types:
            if isinstance(value, t): return value
            continue
        
        if isinstance(value, dict): return self._ondict(value)
        if isinstance(value, list) or isinstance(value, tuple): 
            return self._onlist(value)
        if isinstance(value, AttributeContainer):
            return self._onObject(value)
        
        m = "{!r}".format(value)
        raise NotImplementedError(m)

    
    # example implementations of handlers 
    def _onObject(self, obj):
        descriptors = obj.iterDescriptors()
        for descriptor in descriptors:
            type = descriptor.type
            name = descriptor.name
            value = descriptor.__get__(obj, obj.__class__)
            self.inspect(value)
            continue
        return

    def _ondict(self, value):
        for k, v in value.items():
            v = self.inspect(v)
            continue
        return
    
    def _onlist(self, value):
        for item in value:
            item = self.inspect(item)
            continue
        return 

    
from .AttributeContainer import AttributeContainer

# version
__id__ = "$Id$"

# End of file 
