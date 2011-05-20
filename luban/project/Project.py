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


    visuals = AttributeContainer.descriptors.referenceSet(name='visuals')
    actors = AttributeContainer.descriptors.referenceSet(name='actors')

    name = AttributeContainer.descriptors.str(name='name')


    def identify(self, inspector):
        return inspector.onProject(self)

    

# version
__id__ = "$Id$"

# End of file 
