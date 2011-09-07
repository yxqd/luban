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

    title='A simple example'
    description = [
        """The layout ::

  -----------------------------------------------------
  | top left         | middle            | right      |
  |------------------|                   |            |
  | bottom left      |                   |            |
  -----------------------------------------------------

"""
        ]

    def createDemoPanel(self, **kwds):
        le = lui.e

        #
        frames = le.splitter()
        frames.orientation = 'horizontal'

        # left, middle, right
        frameleft = frames.section(name='left')
        framemiddle = frames.section(name='middle')
        framemiddle.paragraph(text='using Splitter: middle')
        frames.section(name='right').paragraph(text='using Splitter: right')

        # split left to two parts
        insideframe = le.splitter()
        frameleft.append(insideframe)
        insideframe.orientation = 'vertical'
        insideframe.section(name='topleft').paragraph(text='using Splitter: top left')
        insideframe.section(name='bottomleft').paragraph(text='using Splitter: bottom left')
        
        return frames


# End of file 
