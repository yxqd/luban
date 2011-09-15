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

    title='A ReStructuredText document'
    description = [
        ]
    def createDemoPanel(self, **kwds):
        text = '''
Title here
==========

Some more items

* a
* b
        '''
        return lui.e.restructuredtextdocument(text=text)


# End of file 
