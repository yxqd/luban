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


    title='Event "click"'
    description = [
        'A basic document with a onclick event handler.',
        'Click the document to see an alert.',
        ]
    def createDemoPanel(self, **kwds):
        document = luban.e.document(title='click me')
        document.onclick = luban.a.alert('clicked')
        return document


# End of file 
