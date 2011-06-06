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

class Actor(AttributeContainer):


    actorname = descriptors.str(name='actorname')
    content = descriptors.str(name='content')
    

    def identify(self, inspector):
        return inspector.onActor(self)

    

# version
__id__ = "$Id$"

# End of file 
