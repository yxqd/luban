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
    import luban.content
    sometext = luban.content.paragraph(text=['text here'])
        ''',
        ]
    
    abstract = False


    def identify(self, inspector):
        return inspector.onParagraph(self)

    text = base.descriptors.list(name='text')
    text.tip = 'a list of sentences in the paragraph'
    
    contents = base.descriptors.referenceSet(name='contents')
    contents.tip = 'deprecated'
    

# version
__id__ = "$Id"

# End of file 
