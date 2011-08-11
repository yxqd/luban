#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .FormField import FormField as base


class FormSelectorField(base):


    abstract = False


    def identify(self, inspector):
        return inspector.onFormSelectorField(self)

    entries = descriptors.ordered_dict()
    selection = descriptors.str()
    
    

# version
__id__ = "$Id$"

# End of file 
