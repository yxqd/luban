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

from luban import ui as lui

from ....DemoPanelActor import Actor as base
class Actor(base):

    title='A grid'
    description = [
        ]

    def createDemoPanel(self, **kwds):
        doc = lui.e.document(title='test grid')

        doc.paragraph(text='start grid')
        
        grid = doc.grid()

        row0 = grid.row(name='row0')
        row0.cell(name='col0').document(title='row 0, col 0')
        row0.cell(name='col1').document(title='row 0, col 1')
        
        row1 = grid.row(name='row1')
        row1.cell(name='col0').document(title='row 1, col 0')
        row1.cell(name='col1').append('row 1, col 1')
        row1.cell(name='col2').document(title='row 1, col 2')
        row1.cell(name='col3').paragraph(text='row1, col3')
        
        doc.paragraph(text='end grid')
        
        return doc


# End of file 
