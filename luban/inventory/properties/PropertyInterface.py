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


from pyre.inventory.Trait import Trait

class PropertyInterface:

    def _set(self, instance, value, locator):
        # different from pyre.inventory.Property
        # don't do any casting and validation

        # record
        return Trait._set(self, instance, value, locator)


    def _getDefaultValue(self, instance):
        value = self.default

        import pyre.parsing.locators
        locator = pyre.parsing.locators.simple('default')

        return value, locator


    def getValueError(self, value):
        try:
            value = self.convertValue(value)
        except ValueError, e:
            return str(e)
        return


    def convertValue(self, value):
        # it is ok to have no input sometimes
        if self.default is None and (value is None or value is ''): return
        
        try:
            value = self._cast(value)
        except:
            raise ValueError, 'must be a %s' % self.type
        if self.validator:
            value = self.validator(value)
        return value


# version
__id__ = "$Id$"

# End of file 
