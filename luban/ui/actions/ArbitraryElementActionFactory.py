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

"""factory of arbitrary element actions

This could be a mixin base class for SelectingActionBase.
This is however dangerous.
"""


class ArbitraryElementActionFactory:

    
    def __getattr__(self, key):
        # the implementation here allows easy extension of
        # luban element actions. 
        # one can just think of a new element action and use it right away;
        # the following will aways work:
        #   select(id="abc").<actionname>(**parameters)
        # It will create an instance of SimpleElementAction.
        # One just need to make sure the action is handled by
        # the weaver for the media he cares.
        # But this is not the best approach since the API of creating
        # this new action is not clearly coded.
        # It could lead to a lot of confusions.
        from .SimpleElementAction import SimpleElementAction
        def _(**kwds):
            return SimpleElementAction(element=self, actionname=key, **kwds)
        _.__name__ = key
        return _

    pass


# version
__id__ = "$Id$"

# End of file 

