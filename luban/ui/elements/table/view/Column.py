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

# Descriptor of a column
class Column(base):


    measure = descriptors.str(name='measure')
    editable = descriptors.bool(name='editable')
    sortable = descriptors.bool(name='sortable')
    hidden = descriptors.bool(name='hidden')
    label = descriptors.str(name='label')


    def __init__(self, name=None, measure=None, label=None, editable=None, sortable=None, hidden=None):
        if not name:
            name = measure
            
        super(Column, self).__init__(name)
        
        if label is None:
            label = measure
            
        self.label = label
        
        self.measure = measure
        self.editable = editable
        self.sortable = sortable
        self.hidden = hidden
        
        return


    def identify(self, inspector):
        return inspector.onTableViewColumn(self)

    
# version
__id__ = "$Id$"

# End of file 
