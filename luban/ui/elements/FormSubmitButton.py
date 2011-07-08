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


from .Element import Element as base


class FormSubmitButton(base):

    abstract = False


    label = descriptors.str(default='Submit')
    help = descriptors.str()
    tip = descriptors.str()

    def identify(self, inspector):
        return inspector.onFormSubmitButton(self)


# version
__id__ = "$Id$"

# End of file 
