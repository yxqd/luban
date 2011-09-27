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

    title='A simple bulletinboard'
    description = [
        ]

    def createDemoPanel(self, **kwds):
        bb = luban.e.bulletinboard(title="Bulletin board")

        # announcement 1
        announcement1 = bb.announcement(
            title='announcement1',
            date = "today",
            time = "3pm",
            place = "PB 120",
            text = "#@%@#$@#",
            authorlist = "alice and bob",
            )

        return bb


# End of file 
