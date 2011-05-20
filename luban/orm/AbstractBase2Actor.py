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


import luban.content as lc
from luban.content import load, alert, select


from luban.components.AuthorizedActor import AuthorizedActor
from luban.components.FormProcessor import FormProcessorInterface


# convert a abstract base class to an actor
class AbstractBase2Actor(object):


    def __call__(self, AbstractBase, SubClasses, ActorBase=AuthorizedActor):
        class _(FormProcessorInterface, ActorBase):

            class Inventory(FormProcessorInterface.Inventory, ActorBase.Inventory):
                
                identifier = luban.inventory.str('identifier')
                
            
            def _getRecords(self, director):
                ret = []
                orm = director.clerk.orm
                for type in SubClasses:
                    T = orm(type)
                    q = orm.db.query(T)
                    rs = q.all()
                    ret += rs
                    continue
                return ret
        
        return _


import luban.inventory

abstractbase2actor = AbstractBase2Actor()


# version
__id__ = "$Id$"

# End of file 
