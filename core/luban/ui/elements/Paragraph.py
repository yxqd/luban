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

"""
Paragraph

An example of simple UI element.
"""


from .SimpleElement import SimpleElement as base

class Paragraph(base):

    simple_description = 'a paragraph of text'
    full_description = ''
    examples = [
        '''
from luban.ui import e as lue
sometext = lue.paragraph(text=['text here'])
''',
        ]
    

    # attributes
    text = descriptors.str()
    text.tip = 'text in the paragraph'
    
    # for inspector
    def identify(self, inspector):
        return inspector.onParagraph(self)


# version
__id__ = "$Id"

# End of file 
