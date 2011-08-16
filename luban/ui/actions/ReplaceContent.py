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


from .ElementActionBase import ElementActionBase as base

class ReplaceContent(base):


    abstract = False

    #
    factory_method = 'replaceContent'

    # attributes
    newcontent = descriptors.object()

    # for inspector
    def identify(self, inspector):
        return inspector.onReplaceContent(self)



# version
__id__ = "$Id$"

# End of file 

