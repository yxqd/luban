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


class JavaScriptDocument:

    main_enclosure = [
        '$(function (){',
        '});',
        ]

    def identify(self, visitor): return visitor.onJavaScriptDocument(self)

    def __init__(self):
        self.includes = []
        self.main = [] # the main function
        return


    def include(self, script='', scripts=[]):
        if script and scripts:
            raise ValueError

        if script: scripts = [script]
        for s in scripts: self._include(s)
        return
    

    def _include(self, include):
        if include not in self.includes:
            self.includes.append(include)
        return


    pass  # end of JavaScriptDocument


import journal
debug = journal.debug('javascriptdocument')
        


# version
__id__ = "$Id$"

# End of file 
