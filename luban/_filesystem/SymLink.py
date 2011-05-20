# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from File import File

class SymLink(File):


    def identify(self, inspector):
        return inspector.onSymLink(self)


    def __init__(self, name, target=None):
        super(SymLink, self).__init__(name)
        self.target = target
        return



# version
__id__ = "$Id$"

# End of file 
