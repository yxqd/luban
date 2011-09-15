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

    title='A simple example'
    description = [
        """This demo creates the following layout ::

  -----------------------------------------------------
  | top left         | middle            | right      |
  |------------------|                   |            |
  | bottom left      |                   |            |
  -----------------------------------------------------

"""
        ]

    def createDemoPanel(self, **kwds):
        le = luban.e

        #
        frames = le.splitter()
        frames.orientation = 'horizontal'

        # left, middle, right
        frameleft = frames.section(name='left')
        framemiddle = frames.section(name='middle')
        framemiddle.paragraph(text='middle')
        frames.section(name='right').paragraph(text='right')

        # split left to two parts
        insideframe = le.splitter()
        frameleft.append(insideframe)
        insideframe.orientation = 'vertical'
        insideframe.section(name='topleft').paragraph(text='top left')
        insideframe.section(name='bottomleft').paragraph(text='bottom left')
        
        return frames


# End of file 
