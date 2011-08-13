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


from .SimpleElement import SimpleElement as base

class Paragraph(base):

    simple_description = 'a paragraph of texts'
    full_description = ''
    examples = [
        '''
    import luban.ui.elements
    sometext = luban.ui.elements.paragraph(text=['text here'])
        ''',
        ]
    
    abstract = False

    # attributes
    text = descriptors.list()
    text.tip = 'a list of sentences in the paragraph'

    # for inspector
    def identify(self, inspector):
        return inspector.onParagraph(self)


# version
__id__ = "$Id"

# End of file 
