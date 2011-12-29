#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                  Jiao Lin
#                     California Institute of Technology
#                     (C) 2006-2011  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from luban import py_major_ver, setup_context
if py_major_ver == 2: setup_context(locals())


from luban.ui.elements.Riveted import RivetedContainer, Meta, RivetedSubElement
from luban.ui.elements.ElementContainer import buildSubElementFactory


class Slides(RivetedContainer):

    # decorations
    simple_description = 'slide show'
    full_description = ''
    experimental = True
    
    # properties
    timeout = descriptors.int()
    timeout.tip = "milliseconds between slide transitions"

    # methods
    # .. for inspector
    def identify(self, inspector):
        return inspector.onSlides(self)


from luban.ui.elements.SimpleContainer import SimpleContainer
_slidebase = Meta(
    '_slidebase',
    (RivetedSubElement, SimpleContainer),
    {'abstract': 1}
    )
class Slide(_slidebase):
    
    # decorations
    simple_description = 'A slide'
    full_description = ''

    #
    parent_types = [Slides]

    # properties
    caption = descriptors.str()
    
    image = descriptors.str()
    image.tip = 'path of the image'
    
    url = descriptors.str()
    
    # methods
    def identify(self, inspector):
        return inspector.onSlide(self)


Slides.child_types = [Slide]


# subelement factory
buildSubElementFactory('slide', Slide, Slides)


# End of file 
