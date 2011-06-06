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

class Project(AttributeContainer):


    visuals = descriptors.referenceSet(name='visuals')
    actors = descriptors.referenceSet(name='actors')

    name = descriptors.str(name='name')


    def identify(self, inspector):
        return inspector.onProject(self)

    

# version
__id__ = "$Id$"

# End of file 
