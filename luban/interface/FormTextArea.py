#!/usr/bin/env python
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


from FormField import FormField as base


class FormTextArea(base):


    simple_description = 'Text area in a form'
    full_description = ''


    abstract = False


    readonly = base.descriptors.bool(name='readonly')


    def identify(self, inspector):
        return inspector.onFormTextArea(self)


# version
__id__ = "$Id$"

# End of file 
