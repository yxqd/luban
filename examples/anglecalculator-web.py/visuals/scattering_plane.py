# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import luban.content as lc
from luban.content import select, alert, load


def visual():
    doc = lc.document(title='Scattering Plane Vectors')
    doc.Class = 'window'
    
    grid = lc.grid(); doc.add(grid)
    row1 = grid.row(); row2 = grid.row()

    row1.cell().add(inputbox('h1', 'h1'))
    row1.cell().add(inputbox('k1', 'k1'))
    row1.cell().add(inputbox('l1', 'l1'))
    
    row2.cell().add(inputbox('h2', 'h2'))
    row2.cell().add(inputbox('k2', 'k2'))
    row2.cell().add(inputbox('l2', 'l2'))

    return doc


from luban.content.FormTextField import FormTextField
def inputbox(label, name):
    return FormTextField(name=name, label=label)
    

# version
__id__ = "$Id$"

# End of file 
