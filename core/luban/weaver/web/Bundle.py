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


"""
a bundle of libaries

a bundle consists of a base and a bunch of features.

base contains the core libraries needed for all features.
each feature is implemented with some libraries.
"""

class Bundle:

    def __init__(self, base, **features):
        """base: base library names
        **features: pairs of {name: library names}
        """
        self.base = base
        for name, libs in features.items():
            setattr(self, name, libs)
        return


# End of file 
