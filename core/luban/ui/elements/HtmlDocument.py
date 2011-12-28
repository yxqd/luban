#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  
#                                  Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from luban import py_major_ver
if py_major_ver == 2:
    from luban.ui import descriptors


from luban.ui.elements.SimpleElement import SimpleElement
class HtmlDocument(SimpleElement):

    # decorators
    simple_description = 'A simple container of html text'
    full_description = (
        'A htmldocument widget can be used to display simple html-based content. '
        'It cannot handle complex html document with javascript, etc.'
        )

    # properties
    text = descriptors.str()
    text.tip = 'Content of the html document'
    
    # for inspector
    def identify(self, inspector):
        return inspector.onHtmlDocument(self)


# version
__id__ = "$Id$"

# End of file
