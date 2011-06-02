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


from Action import Action as base

class ReplaceContent(base):


    abstract = False


    def identify(self, inspector):
        return inspector.onReplaceContent(self)
    

    element = base.descriptors.reference(name='element')
    newcontent = base.descriptors.reference(name='newcontent')
    


# version
__id__ = "$Id$"

# End of file 

