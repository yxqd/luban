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


def visual(cols=None, editable=True, Class='diffrpeaks-table', id=None):
    if cols is None:
        cols = ['h', 'k', 'l', 'twotheta', 'theta', 'chi', 'phi']

    if not isinstance(editable, dict):
        editable = FakeDict(editable)

    # to construct a table, a model, a view, and a list of data are needed
    from luban.content.table import Model, View, Table
    # first the model
    class model(Model):

        h = Model.descriptors.str(name='h')
        k = Model.descriptors.str(name='k')
        l = Model.descriptors.str(name='l')
        twotheta = Model.descriptors.str(name='twotheta')
        theta = Model.descriptors.str(name='theta')
        chi = Model.descriptors.str(name='chi')
        phi = Model.descriptors.str(name='phi')

    # then the view
    columns = [
        View.Column(label='h', measure='h', editable=editable['h']),
        View.Column(label='k', measure='k', editable=editable['k']),
        View.Column(label='l', measure='l', editable=editable['l']),
        View.Column(label='twotheta', measure='twotheta', editable=editable['twotheta']),
        View.Column(label='theta', measure='theta', editable=editable['theta']),
        View.Column(label='chi', measure='chi', editable=editable['chi']),
        View.Column(label='phi', measure='phi', editable=editable['phi']),
        ]
    columns = filter(lambda c: c.measure in cols, columns)
    view = View(columns = columns, editable = editable)

    # data: a list of rows. each row is a tuple of values for all cells in the row
    # hack: fake data
    data = [ [0]*len(columns) for i in range(2) ]
    
    # now the table
    ret = Table(model=model, data=data, view=view, id=id)
    ret.Class = Class
    return ret



class FakeDict(object):

    
    def __init__(self, v):
        self.v = v

        
    def __getitem__(self, k):
        return self.v

    

# version
__id__ = "$Id$"

# End of file 
