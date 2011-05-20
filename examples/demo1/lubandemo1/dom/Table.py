# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from pyre.db.Table import Table as base


class Table(base):

    def __str__(self):
        columns = self.getColumnNames()
        l = []
        for col in columns:
            value = self.getColumnValue(col)
            l.append('%s=%s' % (col,value))
            continue
        return '[' + ', '.join(l) + ']'

# version
__id__ = "$Id$"

# End of file 
