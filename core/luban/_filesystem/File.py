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


from .Entry import Entry

class File(Entry):


    def identify(self, inspector):
        return inspector.onFile(self)


    def __init__(self, name, content=None, executable=False):
        super(File, self).__init__(name)
        self.content = content
        self.executable = executable
        return



# version
__id__ = "$Id$"

# End of file 
