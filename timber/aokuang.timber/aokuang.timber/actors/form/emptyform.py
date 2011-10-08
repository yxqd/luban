# -*- Python -*-
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

import luban

from ....DemoPanelActor import Actor as base
class Actor(base):

    title='An empty form'
    description = [
        ]
    def createDemoPanel(self, **kwds):
        # form
        form = luban.e.form(title='test form')

        # fields
        # .. check boxes
        checkbox1 = form.checkbox(
            name='boolvar1', label='check box 1', checked=False)

        checkbox2 = form.checkbox(
            name='boolvar2', label='check box 2', checked=True)

        # .. radio box
        choices = ['one', 'two', 'three']
        # entries are a list of (value, description)
        # in simple cases, value could be equal to description
        entries = [(v,v) for v in choices]
        rad = form.radio(
            id='radiofield', label='radio', name='radiovar',
            entries=entries, selection='two',
            )

        # .. selector
        choices = ['alpha', 'beta', 'gamma']
        # entries are a list of (value, description)
        # in simple cases, value could be equal to description
        entries = [(v,v) for v in choices]
        sel = form.selector(
            label='selector', name='selectorvar',
            entries=entries,
            selection='alpha')

        # .. text field
        textfield = form.text(label='textfield', name='textvar')
        
        # .. text area
        textarea = form.textarea(label='textarea', name='textareavar')
        
        # .. password field
        pwfield = form.password(label='password', name='password')

        # fields with validators
        floatfield = form.text(label='float variable', name='floatvar')
        intfield = form.text(label='int variable', name='intvar')
        
        # submit button
        submit = form.submitbutton(label='submit')

        # action when form is submitted
        # Note: The routine "process" is already defined in
        # base class FormProcessorInterface,
        # here we just need to override "_postProcessing".
        form.onsubmit = select(element=form).submit(
            actor = self.name,
            routine = 'process')

        return document



# End of file 
