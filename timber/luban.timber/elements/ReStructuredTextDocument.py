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


class ReStructuredTextDocument(Element):
    
    
    simple_description = 'A simple container of text in ReStructuredText format'
    full_description = (
        'A ReStructuredTextDocument widget can be used to display text'
        'in ReStructuredText format. '
        )
    
    abstract = False
    
    def identify(self, inspector):
        return inspector.onReStructuredTextDocument(self)
    
    text = descriptors.str()
    text.tip = 'Content of the document'


# version
__id__ = "$Id$"

# End of file
