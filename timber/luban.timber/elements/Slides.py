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

from luban.ui.elements.Riveted import RivetedContainer, Meta, RivetedSubElement
from luban.ui.elements.ElementContainer import elementfactory


class Slides(RivetedContainer):

    # decorations
    simple_description = 'slide show'
    full_description = ''
    experimental = True
    
    # properties
    timeout = descriptors.int()
    timeout.tip = "milliseconds between slide transitions"

    # methods
    @elementfactory
    def slide(self, **kwds):
        from luban.ui.elements.SubElementFactory import createSubElement
        return createSubElement(self, Slide, **kwds)
    
    
    def identify(self, inspector):
        return inspector.onSlides(self)


from luban.ui.elements.SimpleContainer import SimpleContainer
class Slide(RivetedSubElement, SimpleContainer, metaclass=Meta):
    
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


# End of file 
