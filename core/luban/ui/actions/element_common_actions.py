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

    'replace content of the selected element with new content'

    # decorations    
    # .. name of action factory method
    factory_method = 'replaceContent'

    # attributes
    newcontent = descriptors.object()

    # for inspector
    def identify(self, inspector):
        return inspector.onReplaceContent(self)



class AddClass(base):

    'add a class to the selected element'

    # decorations
    # .. name of action factory method
    factory_method = 'addClass'

    # attributes
    cls = descriptors.object()

    # for inspector
    def identify(self, inspector):
        return inspector.onAddClass(self)


class RemoveClass(base):

    'remove a class from the selected element'

    # decorations
    # .. name of action factory method
    factory_method = 'removeClass'

    # attributes
    cls = descriptors.object()

    # for inspector
    def identify(self, inspector):
        return inspector.onRemoveClass(self)


class Click(base):

    'click'

    __unique_type_name__ = 'clickaction'

    # decorations    
    # .. name of action factory method
    factory_method = 'click'

    # attributes

    # for inspector
    def identify(self, inspector):
        return inspector.onClickAction(self)



# End of file 
