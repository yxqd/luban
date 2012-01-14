#!/usr/bin/env python
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

from luban import py_major_ver, setup_context
if py_major_ver == 2: setup_context(locals())


from luban.ui.elements.SimpleElement import SimpleElement as base
class SketchCanvas(base):

    # decorations
    simple_description = 'A canvas for a sketch'
    full_description = ('')
    experimental = True

    # properties
    autosave = descriptors.int(default=0)
    autosave.tip = 'if not zero, automatically save the sketch every <auto_save> seconds'

    width = descriptors.int(default=600)
    height = descriptors.int(default=300)
    
    # events
    from luban.ui.Event import Event
    class save(Event):
        # decorations
        simple_description = "event happens when image of sketch is saved" 
        __unique_type_name__ = 'sketchcanvassave'
        # attributes
        data = descriptors.str() # data str
    del Event
    
    
    # methods
    def identify(self, inspector):
        return inspector.onSketchCanvas(self)



# convert data sent from widget to raw binary data
# the input str is created from js canvas.toDataURL
# this implementation breaks the generality of luban widget.
# it should instead send the raw data. or we should try
# to in web controller decode the data before sending
# it to the actor function.
import re, base64
dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
def todata(s):
    imgb64 = dataUrlPattern.match(s).group(2)
    # 
    if py_major_ver == 3:
        imgb64 = imgb64.encode('ascii')
    return base64.b64decode(imgb64)


# End of file 
