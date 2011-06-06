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


from AttributeContainer import AttributeContainer

class Visual(AttributeContainer):


    visualname = descriptors.str(name='visualname')
    visualinstance = descriptors.reference(name='visualinstance')
    

    def identify(self, inspector):
        return inspector.onVisual(self)

    

# version
__id__ = "$Id$"

# End of file 
