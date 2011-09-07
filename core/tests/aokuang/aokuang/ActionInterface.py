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


"""interface factory base class for luban UI object types

decorations to inspect:
* experimental

"""


from luban import ui as lui


from .ObjectInterface import Factory as base
class Factory(base):


    object_type = None # target object type this factory will build interface for
    actor = None # name of the actor for this interface
    demo_panels = None # a list of demo panels, each an instance of DemoPanel
    skip_descriptors = ['lubanaction']
    

# End of file 
