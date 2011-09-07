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

    title='A simple portlet'
    description = [
        'Click on the portlet items to see effects',
        ]

    def createDemoPanel(self, **kwds):
        portlet = lui.e.portlet(title='portlet')

        # item 1
        item1 = portlet.item(label='item1', tip='item1 tip')
        item1.onclick = alert('item1 clicked')

        # item 2
        item2 = portlet.item(label='item2', tip='item2 tip')
        item2.onclick = alert('item2 clicked')

        return portlet


# End of file 
