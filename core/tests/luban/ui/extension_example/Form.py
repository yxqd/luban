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

    abstract = False

    # attributes
    title = descriptors.str()
    title.tip = 'Title of the form'

    onsubmit = descriptors.eventhandler()

    # for inspector
    def identify(self, inspector):
        return inspector.onForm(self)


from luban.ui.actions.ElementActionBase import ElementActionBase
class Submission(ElementActionBase):

    # decorations
    simple_description = 'submit a form to a controller'
    full_description = ()
    abstract = False
    factory_method = "submit"
    element_type = Form
    
    # attributes
    actor = descriptors.str()
    actor.tip = 'The actor that will handle this load action'
    
    routine = descriptors.str()
    routine.tip = 'The routine of the actor that will be called to handle this load action'
    
    params = descriptors.dict()
    params.tip = 'Addtional parameters as a dictionary'
    

    def identify(self, inspector):
        return inspector.onSubmission(self)


# version
__id__ = "$Id$"

# End of file 
