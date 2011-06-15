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


from .DocumentFactory import DocumentFactory
from .ParagraphFactory import ParagraphFactory
from .SimpleContainer import SimpleContainer


class Form(ParagraphFactory, DocumentFactory, SimpleContainer):

    simple_description = 'A container of form fields and a submit button'
    full_description = (
        'Form is a container of form fields and a submit button. '
        'When a form is submitted, data of form fields are posted to the '
        'controller. '
        'A form has a title which can be empty.'
        )

    abstract = False

    def text(self, **kwds):
        from .FormTextField import FormTextField as factory
        element = factory(**kwds)
        self.add(element)
        return element


    def password(self, **kwds):
        from .FormPasswordField import FormPasswordField as factory
        element = factory(**kwds)
        self.add(element)
        return element


    def selector(self, **kwds):
        from .FormSelectorField import FormSelectorField as factory
        element = factory(**kwds)
        self.add(element)
        return element


    def textarea(self, **kwds):
        from .FormTextArea import FormTextArea as factory
        element = factory(**kwds)
        self.add(element)
        return element


    def radio(self, **kwds):
        from .FormRadioBox import FormRadioBox as factory
        element = factory(**kwds)
        self.add(element)
        return element


    def checkbox(self, **kwds):
        from .FormCheckBox import FormCheckBox as factory
        element = factory(**kwds)
        self.add(element)
        return element


    def submitbutton(self, **kwds):
        from .FormSubmitButton import FormSubmitButton as factory
        element = factory(**kwds)
        self.add(element)
        return element


    def identify(self, inspector):
        return inspector.onForm(self)


    title = descriptors.str()
    title.tip = 'Title of the form'

    onsubmit = descriptors.action()
    onsubmit.tip = 'action when the form is submitted'


# version
__id__ = "$Id$"

# End of file 
