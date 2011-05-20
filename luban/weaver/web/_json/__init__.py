# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



def getModule(name):
    'get the wrapper module that wraps the json engine'
    pkg = 'luban.weaver.web._json'
    return __import__('%s._%s' % (pkg, name), {}, {}, [''])


def autodetect():
    'automatic detect the usable json engine'
    try:
        import json
        
    except ImportError:
        try:
            import cjson
        except ImportError:
            raise RuntimeError, 'no json engine available'
        else:
            return 'cjson'
        
    else:
        if 'dumps' in json.__dict__:
            return 'builtin_json'
        if 'write' in json.__dict__:
            return 'json_py'
        
    raise RuntimeError, 'no json engine available'


# version
__id__ = "$Id$"

# End of file 
