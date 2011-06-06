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


import journal
debug = journal.debug('luban.weaver.Content2Dict')
#debug.activate()


from luban._utils import Inherited
from Content2Dict_Extensions import extensions
Extension = Inherited(extensions)


class UIElement2Dict(Extension, object):


    def __init__(self):
        return


    def render(self, element):
        try:
            return element.identify(self)
        except AttributeError, e:
            return self._onElement(element)


    def __getattr__(self, name):
        if name.startswith('on'):
            return self._onElement
        raise
    

    #
    def _onElement(self, element):
        # debug.log('onElement: %s' % (element.__class__.__name__))
        kls = element.__class__
        d = {'type': kls.__name__.lower()}
        
        descriptors = element.iterDescriptors()
        for descriptor in descriptors:
            type = descriptor.type
            name = descriptor.name
            value = descriptor.__get__(element)
            value = self._convertValue(value)
            d[name] = value
            continue

        # mark actions
        if issubclass(kls, Action):
            d['lubanaction'] = 1
        d['lubanelement'] = 1
        return d


    def _convertValue(self, value):
        if isinstance(value, dict): return self._ondict(value)
        if isinstance(value, list) or isinstance(value, tuple): return self._onlist(value)
        if isinstance(value, AttributeContainer): return self.render(value)
        return value


    def _ondict(self, value):
        newvalue = {}
        for k, v in value.iteritems():
            v = self._convertValue(v)
            newvalue[k] = v
            continue
        return newvalue
    def _onlist(self, value):
        newvalue = []
        for item in value:
            item = self._convertValue(item)
            newvalue.append(item)
            continue
        return newvalue


    
from luban.content.AttributeContainer import AttributeContainer
from luban.content.Action import Action

# version
__id__ = "$Id$"

# End of file 
