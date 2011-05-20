#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                  Jiao Lin
#                     California Institute of Technology
#                     (C) 2006-2010  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



from luban._utils import Inherited


from _json import autodetect, getModule
jsonmod = getModule(autodetect())
import traceback
def jsonEncode(o):
    try:
        return jsonmod.encode(o)
    except:
        tb = traceback.format_exc()
        separator = '*'*70 + '\n'
        tb = separator + 'Original exception:\n' + separator + tb + separator
        problematic_elements = jsonFindProblematicElements(o)
        probstr = '\n'.join([' * %s' % e for e in problematic_elements])
        msg =  """json cannot encode %s.\n%s\nThe elements that are problematic are: \n%s\n%s""" % (o, tb, probstr, separator)
        raise RuntimeError, msg


def jsonDecode(o):
    try:
        return jsonmod.decode(o)
    except:
        tb = traceback.format_exc()
        raise RuntimeError, 'json cannot decode %s. Original exception:\n%s' % (o, tb)
     

        
def jsonFindProblematicElements(o, result_set = None):
    '''find the element in the given object that has the problem of json encoding
    '''
    if result_set is None:
        result_set = []
        
    if isinstance(o, list):
        for element in o:
            try:
                jsonEncode(element)
            except:
                jsonFindProblematicElements(element, result_set)
    elif isinstance(o, dict):
        for key,val in o.items():
            try:
                jsonEncode(key)
            except:
                jsonFindProblematicElements(key, result_set)
                
            try:
                jsonEncode(val)
            except:
                jsonFindProblematicElements(val, result_set)
    else:
        result_set.append(o)
    return result_set

# version
__id__ = "$Id$"

# End of file 
