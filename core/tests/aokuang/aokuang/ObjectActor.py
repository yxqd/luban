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

    def default(self):
        title = 'luban demo: %s' % self.title
        f = lui.e.frame(title = title)
        d = self.interface_factory.create()
        f.append(d)
        return f


    def __init__(self, title=None, interface_factory=None):
        self.title = title
        self.interface_factory = interface_factory
        return  


# End of file 
