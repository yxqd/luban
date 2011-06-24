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


import collections
class OrderedDictWithPredefinedSymbols:

    predefined = dict()

    def __init__(self):
        import collections
        self._d = collections.OrderedDict()
        return
    
    
    def __getitem__(self, key):
        d = self._d
        if key in d:
            return d[key]
        return self.predefined[key]


    def __setitem__(self, key, value):
        d = self._d
        d[key] = value
        return value


    def __iter__(self):
        return self._d.__iter__()

    
    def __getattr__(self, key):
        return getattr(self._d, key)



# version
__id__ = "$Id$"

# End of file 
