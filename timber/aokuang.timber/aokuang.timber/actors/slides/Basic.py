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

    title='A basic slideshow'
    description = [
        ]
    def createDemoPanel(self, **kwds):
        slides = luban.e.slides()
        
        slides.slide(caption='slide1', image="slides/super_string_theory.jpg")
        slides.slide(caption='slide2', image="slides/Calabi-Yau_art.jpg")
        return slides


# End of file 
