#!/usr/bin/env python
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

from luban import py_major_ver, setup_context
if py_major_ver == 2: setup_context(locals())



from luban.ui.elements.Riveted import RivetedContainer, Meta, RivetedSubElement
from luban.ui.elements.ElementContainer import buildSubElementFactory


class Grid(RivetedContainer):

    # decorations
    simple_description = 'In essence, a table used for positioning objects in rows and columns'
    full_description = (
        'A grid divides a space into cells. '
        'Widgets can be placed into a grid to achieve '
        'better control the positioning.'
        )
    examples = [
        '''
    grid = luban.ui.e.grid()

    row0 = grid.row()
    row0.cell().document(title='row 0, col 0: a document')
    row0.cell().append(luban.ui.e.form(title='row 0, col 1: a form'))

    row1 = grid.row()
    row1.cell().document(title='row 1, col 0')
    row1.cell().append('row 1, col 1')
    row1.cell().document(title='row 1, col 2')
    row1.cell().append(luban.ui.e.paragraph(text=['row1, col3']))
    ''',
        ]
        

    # methods
    # .. for inspector
    def identify(self, visitor):
        return visitor.onGrid(self)
    


class GridRow(RivetedContainer):

    parent_types = [Grid]

    def identify(self, visitor):
        return visitor.onGridRow(self)
    

from luban.ui.elements.SimpleContainer import SimpleContainer
class GridCell(SimpleContainer):

    parent_types = [GridRow]

    def identify(self, visitor):
        return visitor.onGridCell(self)
    
    pass
    

# only allow GridRow to be children of Grid
Grid.child_types = [GridRow]

# only allow GridCell to be children of GridRow
GridRow.child_types = [GridCell]


# subelement factories
buildSubElementFactory('row', GridRow, Grid)
buildSubElementFactory('cell', GridCell, GridRow)


# version
__id__ = "$Id$"

# End of file 
