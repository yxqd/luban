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

    title='Select a portlet item programmatically'
    description = [
        ]
    def createDemoPanel(self, **kwds):
        # container
        container = luban.e.document()
        #
        p = container.paragraph(id="message")
        # portlet
        portlet = container.portlet()
        #  
        item1 = portlet.item(label='item1', id='portletdemo-select-item1')
        item1.onselect = luban.a.select(element=p).setAttr(text='item1 selected')
        #   item 2
        item2 = portlet.item(label='item2', id='portletdemo-select-item2')
        item2.onselect = luban.a.select(element=p).setAttr(text='item2 selected')
        # controls
        #   button1
        button1 = container.button(
            label='click to choose item1',
            onclick = luban.a.select(element=item1).select()
            )
        #   button2
        button2 = container.button(
            label='click to choose item2',
            onclick = luban.a.select(element=item2).select()
            )
        
        return container



# End of file 
