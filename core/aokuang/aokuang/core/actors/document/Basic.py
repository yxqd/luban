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

    title='Plain document with title'
    description = [
        'A basic document can be created with or without a title.',
        'Subdocuments can be added as children of a document',
        ]
    def createDemoPanel(self, **kwds):
        document = luban.e.document(title='document title')

        # add a paragraph
        p = document.paragraph()
        p.text = 'Hello world!'

        # add a sub document
        subdoc = document.document(title='Subdocument')
        
        return document


# End of file 
