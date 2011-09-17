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

    title='An uploader'
    description = [
        ]

    def createDemoPanel(self, **kwds):
        # create uploader
        uploader = luban.e.uploader(
            name = 'uploaded',
            label='Upload',
            onsubmit=luban.a.load(
                actor=self.name,
                routine='receive_file', id='uploadid-111')
            )
        return uploader


# End of file 
