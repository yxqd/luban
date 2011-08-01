#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

import wx
import wx.lib.buttons as buttons
from .ext import bindCallbacks

events = {
    'click': wx.EVT_BUTTON , 
    }


from .CommonInterface import CommonInterface

class ButtonWithIcon(buttons.GenBitmapTextButton, CommonInterface):

    def __init__(self, parent, id=-1, callbacks = {}, label = 'OK', iconpath=None, size=None):
        # must have at lease one of these: icon or label
        if not label and not iconpath: raise

        # get bitmap
        bitmap = None
        if iconpath:
            bitmap = GetBitmap(iconpath)

        # if no label, make the size small
        if not size and not label and bitmap:
            size = bitmap.GetWidth()+4, bitmap.GetHeight()+4
            
        CommonInterface.__init__(self, parent)

        buttons.GenBitmapTextButton.__init__(self, parent, id=id, bitmap=bitmap, label=label, size=size)
        
        bindCallbacks( self, events, callbacks)
        return
    

    pass # end of ButtonWithIcon


def GetBitmap(path):
    import os
    if not os.path.exists(path): return
    import Image
    source = Image.open(path, 'r')
    image = wx.EmptyImage(*source.size)
    image.SetData( source.convert("RGB").tostring() )
    # if the image has an alpha channel, you can set it with this line:
    image.SetAlphaData(source.convert("RGBA").tostring()[3::4])
    return image.ConvertToBitmap() # wx.BitmapFromImage(image)

# version
__id__ = "$Id$"

# End of file 
