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


class AbstractAttributeContainer(object):

    @classmethod
    def getDescriptors(cls):
        raise NotImplementedError


    @classmethod
    def getDescriptor(cls, name):
        raise NotImplementedError


    def setAttribute(self, name, value):
        raise NotImplementedError


    def getAttribute(self, name):
        raise NotImplementedError


    def iterAttributes(self):
        """iterates over key,value pairs of all attributes
        """
        raise NotImplementedError
    

    def __init__(self, name=None):
        self.name = name
        return

    pass


# version
__id__ = "$Id$"

# End of file 
