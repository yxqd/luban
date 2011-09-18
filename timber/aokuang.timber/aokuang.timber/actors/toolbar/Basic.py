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

    title='A basic toolbar'
    description = [
        'click the buttons to see effects.'
        ]
    def createDemoPanel(self, **kwds):
        # toolbar
        toolbar = luban.e.toolbar()
        # add buttons
        alert = luban.a.alert
        toolbar.button(label='button1', onclick=alert('button1 clicked'))
        toolbar.button(label='button2', onclick=alert('button2 clicked'))
        toolbar.paragraph(Class='spacer')
        toolbar.button(label='button3', onclick=alert('button3 clicked'))
        #
        return toolbar


# End of file 
