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


import journal
debug = journal.debug('luban.weaver.JsonDict2UIElement')
#debug.activate()


from luban._utils import Inherited
from .JsonDict2UIElement_Extensions import extensions
Extension = Inherited(extensions)


class JsonDict2UIElement(Extension): #, object):


    def __init__(self):
        from .uielements import typename2typeMap
        self.typename2type = typename2typeMap()
        return


    def render(self, d):
        if isinstance(d, list) or isinstance(d, tuple):
            return list(map(self.render, d))
            
        if not isinstance(d, dict): return d
        if 'type' not in d: return d
        
        type = d['type']
        type = self.typename2type[type]
        obj = type()
        
        for k, v in d.items():
            if k=='type': continue
            setattr(obj, k, self.render(v))
            continue
        
        return obj



def test1():
    d = {'type': 'document', 'title': 'hello'}
    print(JsonDict2UIElement().render(d))
    return


def test2():
    d = {'type': 'document', 'title': 'hello', 'content':
         [{'type': 'document', 'title': 'subdoc'}]}
    doc = JsonDict2UIElement().render(d)
    print(doc.content)
    return


def main():
    test1()
    test2()
    return


if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# End of file 
