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


from .Action import Action as base

class Loading(base):


    simple_description = 'load from the UI controller'
    full_description = (
        "A 'load' action loads from the UI controller. "
        "The loaded could be some simple data, a luban element, or an action."
        )

    abstract = False


    # attributes
    actor = descriptors.str()
    actor.tip = 'The actor that will handle this load action'
    
    routine = descriptors.str()
    routine.tip = 'The routine of the actor that will be called to handle this load action'

    params = descriptors.dict()
    params.tip = 'Addtional parameters as a dictionary'
    

    def __init__(self, actor=None, routine=None, **params):
        '''load(actor, routine, **kwds) -> load from controller.
        
The given routine of the given actor will be called with additional parameters
specified in the keyword arguments.
'''
        super(Loading, self).__init__(actor=actor, routine=routine, params=params)
        return
    
    
    def identify(self, inspector):
        return inspector.onLoading(self)


# version
__id__ = "$Id$"

# End of file 

