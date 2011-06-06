# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .AttributeContainer import AttributeContainer as base

class View(base):

    from .Column import Column
    
    columns = base.descriptors.referenceSet(name='columns')
    
    editable = base.descriptors.bool(name='editable')
    sortable = base.descriptors.bool(name='sortable')


    def __init__(self, columns, editable=None, sortable=None):
        super(View, self).__init__('view')
        self.columns = columns
        self.editable = editable
        self.sortable = sortable
        return
    
    pass # end of View


# version
__id__ = "$Id$"

# End of file 
