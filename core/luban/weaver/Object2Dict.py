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


from luban import journal
debug = journal.debug('luban.weaver.Object2Dict')


basic_types = int, str, bool

class Object2Dict:

    """renderer to convert an luban object to a dictionary.
    The dictionary rendered will consists of values of
    basic types such as str, integer, and boolean.
    It can also have lists and dictionaries.
    Basically the goal is the result dictionary is json-compatible.
    """

    def render(self, obj):
        try:
            return obj.identify(self)
        except AttributeError as e:
            return self._onObject(obj)


    def convert(self, value):
        if value is None:
            return
        
        for t in basic_types:
            if isinstance(value, t): return value
            continue

        import collections
        if isinstance(value, collections.OrderedDict):
            return self._onordereddict(value)
        if isinstance(value, dict): return self._ondict(value)
        if isinstance(value, list) or isinstance(value, tuple): 
            return self._onlist(value)
        if isinstance(value, AttributeContainer):
            return self.render(value)
        
        m = "{!r}".format(value)
        raise NotImplementedError(m)

    
    def onNoAction(self, obj): return
    def onNoElement(self, obj): return
    

    # luban object type generic handler
    def _onObject(self, obj):
        # debug.log('_onObject: %s' % (obj.__class__.__name__))
        kls = obj.__class__
        d = {'luban_type': kls.__unique_type_name__}
        
        descriptors = obj.iterDescriptors()
        for descriptor in descriptors:
            type = descriptor.type
            name = descriptor.name
            value = descriptor.__get__(obj, obj.__class__)
            value = self.convert(value)
            # skip null value
            if value is None:
                continue
            d[name] = value
            continue

        return d


    # basic types
    def _onordereddict(self, value):
        # json does not have ordered dictionary, render
        # it as a list of tuples
        r = []
        for k,v in value.items():
            v = self.convert(v)
            r.append((k,v))
            continue
        return r
    
    
    def _ondict(self, value):
        newvalue = {}
        for k, v in value.items():
            v = self.convert(v)
            newvalue[k] = v
            continue
        return newvalue
    
    def _onlist(self, value):
        newvalue = []
        for item in value:
            item = self.convert(item)
            newvalue.append(item)
            continue
        return newvalue

    
from luban.ui.AttributeContainer import AttributeContainer
from luban.ui.elements.ElementBase import ElementBase
from luban.ui.actions.ActionBase import ActionBase

# version
__id__ = "$Id$"

# End of file 
