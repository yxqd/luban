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


from PropertyInterface import PropertyInterface
from pyre.inventory.Property import Property

class PropertySet(PropertyInterface, Property):

    def __init__(self, name, pattern, type='str', **kwds):
        Property.__init__(self, name, 'propertyset', **kwds)
        self.pattern = pattern

        import luban.inventory as li
        self.element_descriptor = getattr(li, type)(name, **kwds)
        self._cast = self.element_descriptor._cast


    def convertValue(self, value):
        return self.element_descriptor.convertValue(value)


    # def _set(self, instance, value, locator):
    #     raise NotImplementedError


    def _getDefaultValue(self, instance):
        value = SetProxy(instance, self)

        import pyre.parsing.locators
        locator = pyre.parsing.locators.simple('default')

        return value, locator


class SetProxy(object):


    def __init__(self, instance, descriptor):
        self.instance = instance
        self.descriptor = descriptor
        

    def getPropertyNames(self):
        instance = self.instance
        pattern = self.descriptor.pattern
        return [k for k in instance.__dict__ if pattern.match(k)]


    def getValues(self):
        descriptor = self.descriptor
        ret = {}
        for name in self.getPropertyNames():
            value = getattr(self.instance, name)
            value = descriptor.convertValue(value)
            ret[name] = value
            continue
        return ret


    def getValueErrors(self):
        descriptor = self.descriptor
        es = {}
        for name in self.getPropertyNames():
            value = getattr(self.instance, name)
            e = descriptor.getValueError(value)
            if e: es[name]=e
            continue
        return es



# version
__id__ = "$Id$"

# End of file 
