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


from .ElementContainer import ElementContainer

class Grid(ElementContainer):

    simple_description = 'In essence, a table used for positioning objects in rows and columns'
    full_description = (
        'A grid divides a space into cells. Widgets can be placed into a grid to achieve '
        'better control the positioning.'
        )
    examples = [
        '''
    grid = luban.content.grid()

    row0 = grid.row()
    row0.cell().document(title='row 0, col 0: a document')
    row0.cell().add(luban.content.form(title='row 0, col 1: a form'))

    row1 = grid.row()
    row1.cell().document(title='row 1, col 0')
    row1.cell().add('row 1, col 1')
    row1.cell().document(title='row 1, col 2')
    row1.cell().add(luban.content.paragraph(text=['row1, col3']))
    ''',
        ]
        

    def row(self, **kwds):
        r = GridRow(**kwds)
        self.add(r)
        return r


    def identify(self, visitor):
        return visitor.onGrid(self)
    


class GridRow(ElementContainer):

    def cell(self, **kwds):
        c = GridCell(**kwds)
        self.add(c)
        return c

    def identify(self, visitor):
        return visitor.onGridRow(self)
    

from .DocumentFactory import DocumentFactory
class GridCell(DocumentFactory, ElementContainer):

    def identify(self, visitor):
        return visitor.onGridCell(self)
    
    pass
    

# only allow GridRow to be children of Grid
Grid.allowed_element_types = [GridRow]

# only allow GridCell to be children of GridRow
GridRow.allowed_element_types = [GridCell]


# version
__id__ = "$Id$"

# End of file 
