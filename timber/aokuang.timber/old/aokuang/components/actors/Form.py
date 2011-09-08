#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import luban.content
from luban.content import select, alert, load

from luban.components.FormProcessor import FormProcessorInterface


#from aokuang.components.DemoActor import Actor as base, panel, example, quickpanel
from aokuang.components.WidgetDemoActor import Actor as base, panel, example, quickpanel
class Actor(FormProcessorInterface, base):

    from luban.content.Form import Form as widget

    class Inventory(FormProcessorInterface.Inventory, base.Inventory):

        "variables for the form need to be declared in the inventory"
        
        import luban.inventory

        boolvar1 = luban.inventory.bool(name='boolvar1')
        boolvar2 = luban.inventory.bool(name='boolvar2')
        radiovar = luban.inventory.str(name='radiovar')
        selectorvar = luban.inventory.str(name='selectorvar')
        textvar = luban.inventory.str(name='textvar')
        textareavar = luban.inventory.str(name='textareavar')
        password = luban.inventory.str(name='password')
        floatvar = luban.inventory.float(name='floatvar', validator=luban.inventory.range(10,20))
        intvar = luban.inventory.int(name='intvar', validator=luban.inventory.range(10,20))
        

    introduction = '''
This is a demo of widget "form".
'''

    @quickpanel(
        title = 'Basic usages',
        description =  [
          'Demos here show basic usages of "form" widget, ',        
          ],
        examples = [
          'basic_usage1',
          ],
        )
    def basic_usages(self): pass


    @example(
        title='A simple form',
        description = [
          ],
        deps = [
          'Inventory',
          '_postProcessing',
          ]
        )
    def basic_usage1(self, director):
        lc = luban.content

        # container document
        document = lc.document(title='test form', id='maindoc')

        # form
        form = document.form(title='test form')

        # fields
        checkbox1 = form.checkbox(
            name='boolvar1', label='check box 1', checked=False, tip='a tip')
        checkbox2 = form.checkbox(
            name='boolvar2', label='check box 2', checked=True, tip='a tip')
        rad = form.radio(
            id='radiofield', label='radio', name='radiovar',
            entries=enumerate(['one','two', 'three']), selection=1,
            tip='a tip',
            )
        sel = form.selector(label='selector', name='selectorvar',
                           entries=enumerate(['one','two']),
                            selection=0, tip='a tip')
        textfield = form.text(label='textfield', name='textvar', tip='a tip')
        textarea = form.textarea(label='textarea', name='textareavar', tip='a tip')
        pwfield = form.password(label='password', name='password', tip='a tip')
        # fields with validators
        floatfield = form.text(label='float variable', name='floatvar')
        intfield = form.text(label='int variable', name='intvar')
        
        # submit button
        submit = form.submitbutton(label='submit', tip='a tip')

        # action when form is submitted
        # Note: The routine "process" is already defined in
        # base class FormProcessorInterface,
        # here we just need to override "_postProcessing".
        form.onsubmit = select(element=form).submit(
            actor = self.name,
            routine = 'process')
        
        return document
    

    def _postProcessing(self, director):
        # return a document to show user inputs
        newcontent = luban.content.document(title='form submitted')
        newcontent.paragraph(text=['your form was submitted'])
        # all variables
        names = [
            'boolvar1', 'boolvar2',
            'radiovar',
            'selectorvar',
            'textvar',
            'textareavar',
            'password',
            'floatvar',
            'intvar',
            ]
        # get values
        # values of variables can be accessed thru "self.inventory"
        vals = [getattr(self.inventory, name) for name in names]
        # "print" name
        for k,v in zip(names, vals):
            p = newcontent.paragraph()
            p.text = '%s: %s' % (k,v)
            continue
        # return an action to replace the maindoc with new document
        return select(id='maindoc').replaceContent(newcontent)


# version
__id__ = "$Id$"

# End of file 
