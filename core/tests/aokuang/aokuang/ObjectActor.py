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


from luban.controller.Actor import Actor as base
class Actor(base):

    frame_title = None # title of the frame
    interface_factory = None # interface factory
    
    def default(self):
        # frame
        title = self.frame_title
        f = lui.e.frame(title = title)
        
        # interior
        self.interface_factory.actor = self.name
        d = self.interface_factory.create()
        
        f.append(d)
        return f


# End of file 
