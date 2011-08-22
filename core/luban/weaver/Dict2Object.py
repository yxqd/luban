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


from luban import journal
debug = journal.debug('luban.weaver.Dict2Object')
#debug.activate()


class Dict2Object:


    def __init__(self):
        from ..ui.meta.TypeRegistryCurator import registry
        self.typename2type = registry
        return


    def render(self, d):
        if isinstance(d, list) or isinstance(d, tuple):
            return list(map(self.render, d))
            
        if not isinstance(d, dict): return d
        if 'type' not in d: return d
        
        type = d['type']
        type = self.typename2type.get(type)
        obj = type()
        
        for k, v in d.items():
            if k=='type': continue
            setattr(obj, k, self.render(v))
            continue
        
        return obj



# version
__id__ = "$Id$"

# End of file 
