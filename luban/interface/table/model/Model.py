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


from luban.content.Element import Element as base

class Model(base):

    #name = None ?
    row_identifiers = [] #measures that, when combined together, can be used to uniquely identify a row

    import descriptors
    
    pass


def test():
    class MyModel(Model):
        a = Model.descriptors.time(name='a')
        b = Model.descriptors.str(name='b')
    return


# version
__id__ = "$Id$"

# End of file 
