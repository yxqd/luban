#!/usr/bin/env python
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


from Element import Element


class Canvas(Element):


    def identify(self, inspector):
        return inspector.onCanvas(self)



#class DialogActions(object):
#
#
#    def dialog(self, actionname, **kwds):
#        from SimpleElementAction import SimpleElementAction
#        return SimpleElementAction(self, actionname, **kwds)


# version
__id__ = "$Id$"

# End of file
