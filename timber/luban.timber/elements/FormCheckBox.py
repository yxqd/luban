#!/usr/bin/env python
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


from .FormField import FormField as base


class FormCheckBox(base):


    abstract = False


    checked = descriptors.bool()
    value = descriptors.bool()
    
    
    def identify(self, inspector):
        return inspector.onFormCheckBox(self)


# version
__id__ = "$Id$"

# End of file 