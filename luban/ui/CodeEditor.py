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


from .Element import Element


class CodeEditor(Element):

    simple_description = 'A widget for editing a piece of code'
    full_description = (
        'A CodeEditor widget can be used to edit a piece of code.'
        )
    
    abstract = False
    experimental = True

    def identify(self, inspector):
        return inspector.onCodeEditor(self)

    syntax = Element.descriptors.str(name='syntax')
    syntax.tip = 'Syntax of the code. python, c++, etc'
    
    text = Element.descriptors.str(name='text')
    text.tip = 'Text of the code'

    onsave = Element.descriptors.eventHandler(name='onsave')
    onsave.tip = 'event handler that triggers when user clicks the save button of the widget'
    
    onchange = Element.descriptors.eventHandler(name='onchange')
    onchange.tip = 'event handler that triggers when user changes the text in the widget and the widget lost focus'
    

# version
__id__ = "$Id$"

# End of file
