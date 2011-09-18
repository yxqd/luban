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

    title='A basic "tabs" widget'
    description = [
        'A tabs container widget can be created using "tabs" factory method,',
        'and then tabs can be added to the container.',
        'Please click on the tabs to see it working.',
        ]
    def createDemoPanel(self, **kwds):
        tabs = luban.e.tabs()
        tabs.tab('tab1').paragraph(text='tab1 texts')
        tabs.tab('tab2', selected=1).paragraph(text='tab2 texts')
        tabs.tab('tab3').paragraph(text='tab3 texts')
        return tabs


# End of file 
