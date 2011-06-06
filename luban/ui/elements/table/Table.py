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


from luban.content.Element import Element


class Table(Element):

    simple_description = 'An organized way of display large amount of data'
    full_description = (
        "A table is different from a grid. "
        "It is used to display a number of records, all of which have the "
        "same attributes (columns). "
        "Conceptually you can regard it as a view of a database table. "
        )

    abstract = False
    
    model = descriptors.reference(name='model')
    view = descriptors.reference(name='view')
    data = descriptors.lists(name='data')
    oncellchanged = descriptors.reference(name='oncellchanged')


    def __init__(self, model=None, data=None, view=None, **kwds):
        Element.__init__(self, model=model, data=data, view=view, **kwds)
        return
    
    def identify(self, visitor): return visitor.onTable(self)

    pass # end of Table


from . import TableActions


def example():
    from .model.Model import Model
    class model(Model):
        
        title = descriptors.str(name='title')
        date = descriptors.date(name='date')

    data = [
        ( 'abc', '06/06/2006' ),
        ( 'hi', '05/05/2005' ),
        ]

    from .view.View import View as View
    view = View(
        columns = [
        View.Column(name='col1',label='Title', measure='title'),
        View.Column(name='col2',label='Date', measure='date', editable=True),
        ],
        editable = True,
        )

    table = Table(model, data, view)
    print(table.id)
    return table


def test():
    table = example()
    return


def main():
    test()
    return

if __name__ == '__main__': main()
    

# version
__id__ = "$Id$"

# End of file 
