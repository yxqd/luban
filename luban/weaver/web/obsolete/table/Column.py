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


class Column:

    def __init__(self, name, label, datatype, editable=False, **kwds):
        '''Descriptor of column
        name: name of the column. this must be unique among columns
        label: label to be shown for the column
        datatype: data type of the column
        editable: editable or not
        '''
        self.name = name
        self.label = label
        self.datatype = datatype
        self.editable = editable
        self.options = kwds
        return


# version
__id__ = "$Id$"

# End of file 
