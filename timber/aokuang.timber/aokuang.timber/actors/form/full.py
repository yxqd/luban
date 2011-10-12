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

    title='A form'
    description = [
        "This is a form with a few typical form controls.",
        "You can change the values of these form controls, ",
        "and then submit the form.",
        ]
    rank = 0
    

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
            selection='gamma')

        # .. text field
        textfield = form.text(label='textfield', name='textvar')
        
        # .. text area
        textarea = form.textarea(label='textarea', name='textareavar')
        
        # .. password field
        pwfield = form.password(label='password', name='password')

        # submit button
        submit = form.submitbutton(label='submit')

        # action when form is submitted
        # since the event handler "onsubmit" is reponsible for the submssion
        # event, "luban.event.data" refers to the form data.
        form.onsubmit = luban.a.load(
            actor = self.name,
            routine = 'process',
            kwds = luban.event.data,
            )

        return form

    
    def process(self, **kwds):
        msg = "submitted: %s" % (kwds,)
        return luban.a.alert(msg)


# End of file 
