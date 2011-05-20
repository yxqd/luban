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


'''abstract base class for actor
'''


class Actor(object):


    def select(self, id=None, type=None, **kwds):
        return self.Selector(id=id, type=type, **kwds)

    from SelectorBase import Selector
    

    def getAlert(self):
        raise NotImplementedError
    
    
    def sleep(self, seconds):
        time.sleep(seconds)
        return


import time

# version
__id__ = "$Id$"

# End of file 

