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

    # decorations    
    # .. name of action factory method
    factory_method = 'replaceContent'

    # attributes
    newcontent = descriptors.object()

    # for inspector
    def identify(self, inspector):
        return inspector.onReplaceContent(self)



class AddClass(base):

    # decorations
    # .. name of action factory method
    factory_method = 'addClass'

    # attributes
    cls = descriptors.object()

    # for inspector
    def identify(self, inspector):
        return inspector.onAddClass(self)


class RemoveClass(base):

    # decorations
    # .. name of action factory method
    factory_method = 'removeClass'

    # attributes
    cls = descriptors.object()

    # for inspector
    def identify(self, inspector):
        return inspector.onRemoveClass(self)


# End of file 
