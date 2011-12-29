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


from luban import py_major_ver, setup_context
if py_major_ver == 2: setup_context(locals())


from luban.ui.elements.SimpleElement import SimpleElement as base
class FormSubmitButton(base):

    # attributes
    label = descriptors.str(default='Submit')
    help = descriptors.str()
    # XXX: not supported yet
    # tip = descriptors.str()

    # methods
    def identify(self, inspector):
        return inspector.onFormSubmitButton(self)


# version
__id__ = "$Id$"

# End of file 
