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
    doc = lc.document(title='Lattice Parameters')
    doc.Class = 'window'
    
    grid = lc.grid(); doc.add(grid)
    row1 = grid.row(); row2 = grid.row()

    row1.cell().add(inputbox('a', 'a'))
    row1.cell().add(inputbox('b', 'b'))
    row1.cell().add(inputbox('c', 'c'))
    
    row2.cell().add(inputbox('alpha', 'alpha'))
    row2.cell().add(inputbox('beta', 'beta'))
    row2.cell().add(inputbox('gamma', 'gamma'))

    doc.add(inputbox('Wavelength (angsrom)', 'wavelength'))
    return doc


from luban.content.FormTextField import FormTextField
def inputbox(label, name):
    return FormTextField(name=name, label=label)
    

# version
__id__ = "$Id$"

# End of file 
