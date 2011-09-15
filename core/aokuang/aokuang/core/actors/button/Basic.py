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

from luban import ui as lui

from ....DemoPanelActor import Actor as base
class Actor(base):

    title='A simple button'
    description = [
        'Click the button to see an alert',
        ]
    def createDemoPanel(self, **kwds):
        button = lui.e.button(
            label = 'click me',
            onclick = lui.a.alert('clicked button'),
            )
        return button


# End of file 
