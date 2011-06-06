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


from .Element import Element

class Credential(Element):


    abstract = False

    username = Element.descriptors.str(name='username')
    ticket = Element.descriptors.str(name='ticket')


    def identify(self, visitor):
        return visitor.onCredential(self)
    
    
# version
__id__ = "$Id$"

# End of file 
