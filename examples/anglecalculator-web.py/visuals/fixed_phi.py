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
    doc = lc.document(title='Fixed Phi Value')
    doc.Class = 'window'
    
    grid = lc.grid(); doc.add(grid)
    row1 = grid.row()

    row1.cell().add(inputbox('Fixed Phi', 'fixed_phi'))
    return doc


from luban.content.FormTextField import FormTextField
def inputbox(label, name):
    return FormTextField(name=name, label=label)
    

# version
__id__ = "$Id$"

# End of file 
