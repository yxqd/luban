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


from luban import py_major_ver, setup_context
if py_major_ver == 2: setup_context(locals())


from .FormField import FormField as base
class FormTextArea(base):

    # decorations
    simple_description = 'Text area in a form'
    full_description = ''
    

    # attributes
    readonly = descriptors.bool()
    
    
    def identify(self, inspector):
        return inspector.onFormTextArea(self)


# version
__id__ = "$Id$"

# End of file 
