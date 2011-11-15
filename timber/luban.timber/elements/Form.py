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
    def text(self, **kwds):
        from .FormTextField import FormTextField as factory
        from luban.ui.elements.SubElementFactory import createSubElement
        return createSubElement(self, factory, **kwds)
    
    
    def password(self, **kwds):
        from .FormPasswordField import FormPasswordField as factory
        from luban.ui.elements.SubElementFactory import createSubElement
        return createSubElement(self, factory, **kwds)


    def selector(self, **kwds):
        from .FormSelectorField import FormSelectorField as factory
        from luban.ui.elements.SubElementFactory import createSubElement
        return createSubElement(self, factory, **kwds)


    def textarea(self, **kwds):
        from .FormTextArea import FormTextArea as factory
        from luban.ui.elements.SubElementFactory import createSubElement
        return createSubElement(self, factory, **kwds)


    def radio(self, **kwds):
        from .FormRadioBox import FormRadioBox as factory
        from luban.ui.elements.SubElementFactory import createSubElement
        return createSubElement(self, factory, **kwds)


    def checkbox(self, **kwds):
        from .FormCheckBox import FormCheckBox as factory
        from luban.ui.elements.SubElementFactory import createSubElement
        return createSubElement(self, factory, **kwds)


    def submitbutton(self, **kwds):
        from .FormSubmitButton import FormSubmitButton as factory
        from luban.ui.elements.SubElementFactory import createSubElement
        return createSubElement(self, factory, **kwds)


    def identify(self, inspector):
        return inspector.onForm(self)




# definition of fields
from .FormTextField import FormTextField
from .FormPasswordField import FormPasswordField
from .FormTextArea import FormTextArea
from .FormSubmitButton import FormSubmitButton
from .FormSelectorField import FormSelectorField
from .FormRadioBox import FormRadioBox
from .FormCheckBox import FormCheckBox



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


# version
__id__ = "$Id$"

# End of file 
