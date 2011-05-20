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


from Element import Element as base


class FormSubmitButton(base):

    abstract = False


    label = base.descriptors.str(name='label', default='Submit')
    help = base.descriptors.str(name='help')
    tip = base.descriptors.str(name='tip')

    def identify(self, inspector):
        return inspector.onFormSubmitButton(self)


# version
__id__ = "$Id$"

# End of file 
