# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from UIApp import UIApp as Base, Activity


class CliApplication(Base):


    def main(self, *args, **kwds):
        return self._main(*args, **kwds)

    
    def render(self, visual=None):
        print visual
        return visual


# version
__id__ = "$Id$"

# End of file 
