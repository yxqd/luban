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


from luban.ui.elements.SimpleElement import SimpleElement as base
class FormField(base):

    simple_description = "base of form fields"
    full_description = ""

    label = descriptors.str(default='label')
    help = descriptors.str(default='')
    # XXX: not supported yet
    # tip = descriptors.str(default='')
    error = descriptors.str(default='')
    value = descriptors.str(default='')
    required = descriptors.bool()

    # events
    # events -- must have one-one correspondence with event handler
    from luban.ui.Event import Event
    # change
    class change(Event):
        # decorations
        simple_description = "happens when field value changed"
        __unique_type_name__ = 'formfieldchange'
        # attributes
        old = descriptors.str()
        new = descriptors.str()
    # focus
    class focus(Event):
        # decorations
        simple_description = "happens when focusd"
        __unique_type_name__ = 'formfieldfocus'
        # attributes
    # blur
    class blur(Event):
        # decorations
        simple_description = "happens when lost focus"
        __unique_type_name__ = 'formfieldblur'
        # attributes
    del Event


# to define a new element action, subclass ElementActionBase
from luban.ui.actions.ElementActionBase import ElementActionBase
class FormFieldShowError(ElementActionBase):

    "show error message for a form field"

    # decorations
    element_type = FormField
    factory_method = "showError"

    # properties
    message = descriptors.str()
    
    # methods
    def identify(self, visitor):
        return visitor.onFormFieldShowError(self)

# version
__id__ = "$Id$"

# End of file 
