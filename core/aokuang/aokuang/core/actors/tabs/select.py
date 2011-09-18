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

    title='Select a tab programmatically'
    description = [
        'Click the buttons to select tabs',
        ]
    def createDemoPanel(self, **kwds):
        # container
        container = luban.e.document()
        #
        p = container.paragraph(id="message")
        # tabs
        tabs = container.tabs()
        #   tab 1
        tab1 = tabs.tab(label='tab1', id='tabdemo-select-tab1')
        tab1.onselect = luban.a.select(element=p).setAttr(text='tab1 selected')
        #   tab 2
        tab2 = tabs.tab(label='tab2', id='tabdemo-select-tab2')
        tab2.onselect = luban.a.select(element=p).setAttr(text='tab2 selected')
        # controls
        #   button1
        button1 = container.button(
            label='click to choose tab1',
            onclick = luban.a.select(element=tab1).select()
            )
        #   button2
        button2 = container.button(
            label='click to choose tab2',
            onclick = luban.a.select(element=tab2).select()
            )
        
        return container



# End of file 
