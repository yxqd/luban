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

# only necessary if using python2
from luban import py_major_ver, setup_context
if py_major_ver == 2: setup_context(locals())


from luban.ui.elements.SimpleContainer import SimpleContainer
class Form(SimpleContainer):

    # decorations
    simple_description = 'A container of form fields and a submit button'
    full_description = (
        'Form is a container of form fields and a submit button. '
        'When a form is submitted, data of form fields are posted to the '
        'controller. '
        'A form has a title which can be empty.'
        )

    abstract = False

    # attributes
    title = descriptors.str()
    title.tip = 'Title of the form'

    # for inspector
    def identify(self, inspector):
        return inspector.onForm(self)


# version
__id__ = "$Id$"

# End of file 
