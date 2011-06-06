#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .SimpleContainer import SimpleContainer


class HtmlDocument(SimpleContainer):


    simple_description = 'A simple container of html text'
    full_description = (
        'A htmldocument widget can be used to display simple html-based content. '
        'It cannot handle complex html document with javascript, etc.'
        )

    abstract = False

    def identify(self, inspector):
        return inspector.onHtmlDocument(self)

    text = descriptors.list(name='text')
    text.tip = 'Content of the html document'
    
    title = descriptors.str(name='title')
    title.title = 'Title of the document'


# version
__id__ = "$Id$"

# End of file
