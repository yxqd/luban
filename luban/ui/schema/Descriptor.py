# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


from .Object import Object


# declaration
class Descriptor:
    """
    The base class for typed descriptors

    Descriptors are class data members that enable special processing to occur whenever they
    are accessed as attributes of class instances. For example, descriptors that define the
    methods __get__ and __set__ are recognized by the python interpreter as data access
    interceptors. 
    """


    # class public data
    name = None # my name
    default = None # my default value
    optional = False # am i allowed to be uninitialized?
    type = Object # my type


# end of file 
