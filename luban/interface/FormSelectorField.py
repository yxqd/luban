#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from FormField import FormField as base


class FormSelectorField(base):


    abstract = False


    def identify(self, inspector):
        return inspector.onFormSelectorField(self)

    entries = base.descriptors.lists(name='entries')
    selection = base.descriptors.str(name='selection')
    
    

# version
__id__ = "$Id$"

# End of file 
