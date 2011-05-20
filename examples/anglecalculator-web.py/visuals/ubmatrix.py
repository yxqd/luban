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
    doc = lc.document(title='UB matrix', id='ubmatrix-doc')
    grid = lc.grid(); doc.add(grid)

    row1 = grid.row()
    row1.cell().add(inputbox('ub11'))
    row1.cell().add(inputbox('ub12'))
    row1.cell().add(inputbox('ub13'))
    
    row2 = grid.row()
    row2.cell().add(inputbox('ub21'))
    row2.cell().add(inputbox('ub22'))
    row2.cell().add(inputbox('ub23'))
    
    row3 = grid.row()
    row3.cell().add(inputbox('ub31'))
    row3.cell().add(inputbox('ub32'))
    row3.cell().add(inputbox('ub33'))
    
    return doc
    
from luban.content.FormTextField import FormTextField
def inputbox(name):
    return FormTextField(name=name)
    

# version
__id__ = "$Id$"

# End of file 
