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

    # decorations

    # attributes
    checked = descriptors.bool()
    value = descriptors.bool() # overload the common value descriptor: type is bool
    
    # methods
    def identify(self, inspector):
        return inspector.onFormCheckBox(self)


# End of file 
