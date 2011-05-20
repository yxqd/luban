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


# base class for all molds
# a mold is used by painter to paint a particular type of object. 


class MoldBase(object):


    def __init__(self, orm, actor):
        '''
        orm: object->db mapper
        '''
        self.orm = orm
        self.actor = actor
        return
    

    def __call__(self, obj):
        raise NotImplementedError


# version
__id__ = "$Id$"

# End of file 
