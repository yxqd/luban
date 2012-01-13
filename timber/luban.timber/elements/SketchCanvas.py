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
    auto_save = descriptors.int(default=0)
    auto_save.tip = 'if not zero, automatically save the sketch every <auto_save> seconds'

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


# End of file 
