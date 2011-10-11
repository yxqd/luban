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

class Directory(Entry):


    def identify(self, inspector):
        return inspector.onDirectory(self)


    def addEntry(self, entry):
        self.entries[entry.name] = entry
        return


    def __init__(self, name):
        super(Directory, self).__init__(name)
        
        self.entries = {}
        return

    
    def __getitem__(self, name):
        if name.find('/') == -1:
            return self.entries[name]
        tokens = name.split('/')
        top = tokens[0]
        subdir = self[top]
        return subdir['/'.join(tokens[1:])]


# End of file 
