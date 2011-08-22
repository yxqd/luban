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


# renders a luban ui instance to a json representation

class JsonReprRenderer:

    """This mill creates html or json output from a luban ui model.

    luban ui model is represented by a hierarchy of luban ui objects.
    
    The renderer first 
    """

    def __init__(self):
        from luban.weaver.Object2Dict import Object2Dict
        self._obj2dict = Object2Dict()
        return


    # set obj2dict to provide custom behavior
    @property
    def obj2dict(self): return self._obj2dict
    @obj2dict.setter
    def _set_obj2dict(self, obj2dict):
        self._obj2dict = obj2dict
        return obj2dict

    
    def render(self, obj):
        asdict = self._obj2dict.convert(obj)
        injson = jsonEncode(asdict)
        return injson



from ._utils import jsonEncode

from luban import journal
debug = journal.debug('luban.weaver.web')


# End of file 
