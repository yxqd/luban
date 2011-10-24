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

    title='"oncreate" event'
    description = [
        '"oncreate" event happens when an element is created.',
        ]
    rank = 1
    
    def createDemoPanel(self, **kwds):
        doc = luban.e.document(title='container', id='oncreate-demo-container')
        p = luban.e.paragraph(text='appended when document is created')
        doc.oncreate = luban.a.select(element=doc).append(newelement=p)
        return doc


# End of file 
