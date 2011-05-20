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

class Table:

    def __init__(self, column_descriptors, rows=None, oncellchanged=None, row_identifiers=None):
        '''
        column_descriptors: descriptors of columns
        rows: list of rows. Each row is a list, in which each element is the value of the corresponding column
        oncellchanged: callback function for cell-changed event
        row_identifiers: a list of column names that, when combined together, can be used to uniquely identify a row
        '''

        self.column_descriptors = column_descriptors

        if rows is None: rows = []
        self.rows = rows

        self.oncellchanged = oncellchanged
        self.row_identifiers = row_identifiers
        return


    def identify(self, visitor):
        return visitor.onTable(self)


    def addRow(self, *row):
        self.rows.append( row )
        return



def test():
    from Column import Column
    cols = [
        Column( 'col1', 'Title', 'text' ),
        Column( 'col2', 'Date', 'date', valid_range = [ '01/01/1977', '01/01/2008' ] ),
        ]
    table = Table( cols )
    table.addRow( 'abc', '06/06/2006' )
    table.addRow( 'hi', '05/05/2005' )
    return

if __name__ == '__main__': test()


# version
__id__ = "$Id$"

# End of file 
