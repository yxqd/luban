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



from luban.ui.elements.SimpleContainer import SimpleContainer, Meta
class Form(SimpleContainer, metaclass=Meta):

    # decorations
    simple_description = 'A container of form fields and a submit button'
    full_description = (
        'Form is a container of form fields and a submit button. '
        'When a form is submitted, data of form fields are posted to the '
        'controller. '
        'A form has a title which can be empty.'
        )

    # properties
    title = descriptors.str()
    title.tip = 'Title of the form'

    # events
    # events -- must have one-one correspondence with event handler
    from luban.ui.Event import Event
    class submit(Event):
        # decorations
        simple_description = "form submission event"
        __unique_type_name__ = 'submit'
        # attributes
        data = descriptors.dict()
        data.tip = "form data"
    del Event
    

    # methods
    # .. for inspector
    def identify(self, inspector):
        return inspector.onForm(self)

    # overload _isAContainerOf to provide custom behavior
    @classmethod
    def _isAContainerOf(cls, type):
        if type is Form:
            return False
        return super()._isAContainerOf(type)


    # overload elementfactories to provide custom behavior
    @classmethod
    def elementfactories(cls):
        factories = super().elementfactories()
        # omit the factories that are already defined below
        return [name for name in factories if not name.startswith('form')]


# definition of fields
from .FormTextField import FormTextField
from .FormPasswordField import FormPasswordField
from .FormTextArea import FormTextArea
from .FormSubmitButton import FormSubmitButton
from .FormSelectorField import FormSelectorField
from .FormRadioBox import FormRadioBox
from .FormCheckBox import FormCheckBox


# subelement factories
from luban.ui.elements.ElementContainer import buildSubElementFactory
buildSubElementFactory('text', FormTextField, Form)
buildSubElementFactory('password', FormPasswordField, Form)
buildSubElementFactory('selector', FormSelectorField, Form)
buildSubElementFactory('textarea', FormTextArea, Form)
buildSubElementFactory('radio', FormRadioBox, Form)
buildSubElementFactory('checkbox', FormCheckBox, Form)
buildSubElementFactory('submitbutton', FormSubmitButton, Form)


# actions
# to define a new element action, subclass ElementActionBase
from luban.ui.actions.ElementActionBase import ElementActionBase
class FormSubmission(ElementActionBase):

    "submit a form"

    # decorations
    element_type = Form
    factory_method = "submit"
    
    # methods
    def identify(self, visitor):
        return visitor.onFormSubmission(self)


class FormClearErrors(ElementActionBase):

    "clear error messages in the form"

    # decorations
    element_type = Form
    factory_method = "clearErrors"
    
    # methods
    def identify(self, visitor):
        return visitor.onFormClearErrors(self)


# version
__id__ = "$Id$"

# End of file 
