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


"""
button
"""

import luban.ui as lui

from luban.controller.Actor import Actor as base
class Actor(base):

    expose = 1

    
    def default(self):
        return self.frame()
    

    def frame(self):
        frame = lui.e.frame(title="luban test: button")
        doc = frame.document(title="Click the following button")
        b = doc.button(
            label = 'button 1',
            onclick = lui.a.alert('clicked button 1'),
            )
        b2 = doc.button(
            label = 'button 2',
            onclick = lui.a.load(actor=self.name, routine='onb2'),
            )
        return frame


    def onb2(self):
        return lui.a.alert("clicked button 2")



# End of file 

