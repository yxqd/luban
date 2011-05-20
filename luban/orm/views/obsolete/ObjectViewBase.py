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


# base class for all view factories

class Factory(object):


    def __init__(self, orm, tools):
        self.orm = orm
        self.tools = tools
        return
    

    def __call__(self, obj):
        raise NotImplementedError


    def _newFactory(self, ctor):
        return ctor(self.orm, self.tools)
        

# version
__id__ = "$Id$"

# End of file 
