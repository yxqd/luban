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


from luban.ui.elements.SimpleElement import SimpleElement


class ReStructuredTextDocument(SimpleElement):
    
    # decorations
    simple_description = 'A simple container of text in ReStructuredText format'
    full_description = (
        'A ReStructuredTextDocument widget can be used to display text'
        'in ReStructuredText format. '
        )
    # .. this is a real luban type
    abstract = False
    
    # properties
    text = descriptors.str()
    text.tip = 'Content of the document'


    # methods
    # .. for inspector
    def identify(self, inspector):
        return inspector.onReStructuredTextDocument(self)


# this is a temporary solution
# we should have a better way to handle ReStructuredText
# but for now we just convert it to html
def reSTdoc2htmldoc(restdoc):
    rest = restdoc.text
    from ..utils.rst import rest2html
    html = rest2html(rest)
    kls = restdoc.Class
    if 'ReST' not in kls: kls.append('ReST')
    from luban import ui as lui
    htmldoc = lui.htmldocument(text=html, id=restdoc.id or '', Class=kls)
    return htmldoc
def onReStructuredText(self, doc):
    htmldoc = reSTdoc2htmldoc(doc)
    return self.render(htmldoc)
from luban.weaver.Object2Dict import Object2Dict
Object2Dict.onReStructuredText = onReStructuredText


# version
__id__ = "$Id$"

# End of file