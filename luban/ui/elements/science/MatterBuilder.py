#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                     California Institute of Technology
#                       (C) 2008  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

#from luban.content.Element import Element

from luban.content.SimpleContainer import SimpleContainer

#from luban.content.Document import Document

class MatterBuilderConstructor(SimpleContainer.__metaclass__):
    """meta class for MatterBuilder to collect all the functions in vimm.vimmLib
    and set them up as methods of MatterBuilder.
    
    On second thought, should probably switch this to vimm.Frame in near future...then can access
    all individual builders.
    """    

    def __init__(MatterBuilderClass, name, bases, dict):
        type.__init__(MatterBuilderClass, name, bases, dict)
##         #import vimm.vimmLib as v
##         for attribute in dir(v):
##             # put all the objects in MatterBuilder except vimmLib's __whatever__ attributes
##             if attribute[:2]!='__':
##                 dict[attribute] = v.__dict__[attribute]
##                 # or could have done it this way
##                 #setattr(MatterBuilderClass, attribute, v.__dict__[attribute])

class MatterBuilder(SimpleContainer):
    """Here is an example of how to use MatterBuilder

    >>> from luban.content.science.MatterBuilder import MatterBuilder
    >>> matterBuilder = MatterBuilder()
    >>> 
    >>> 
    >>> 
    >>> 
    
    All the methods in vimm.vimmLib are available in MatterBuilder
    through the use of MatterBuilderConstuctor, it's metaclass.
    """

    simple_description = 'widget to show a atomic structure'
    full_description = 'MatterBuilder can be used to show configurations of atomic sytems such as crystals, molecules, or complex disordered materials.'

    experimental = True
    abstract = False

#    matter = descriptors.referenceSet()

    # this is temporary. need to think about this more
    lattice = descriptors.lists()
    atoms = descriptors.lists()
    
    # make it so it can accept Structure data objects--do this in the actor for now
    # create an actor in luban for matter builder..
    # tell Jiao so he can hook it up to view arbitrary structures
    # make it so it renders different atoms    

    def identify(self, visitor):
        return visitor.onMatterBuilder(self)
    
    #__metaclass__ = MatterBuilderConstructor


        
        
    

# version
__id__ = "$Id$"

# End of file 
