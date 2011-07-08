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


from luban.ui.elements.Element import Element as base

class Model(base):

    #name = None ?
    row_identifiers = [] #measures that, when combined together, can be used to uniquely identify a row

    from . import descriptors
    
    pass


def test():
    class MyModel(Model):
        a = descriptors.time()
        b = descriptors.str()
    return


# version
__id__ = "$Id$"

# End of file 
