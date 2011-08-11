# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


class CastingError(Exception):
    """
    Exception raised on failed attempts to convert a value to one of the supported types
    """

    def __init__(self, value, description, **kwds):
        super().__init__(**kwds)
        self.description = description
        self.value = value
        return


# end of file 
