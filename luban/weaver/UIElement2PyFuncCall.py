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
debug = journal.debug('luban.weaver.UIElement2PyFuncCall')
#debug.activate()


# convert a ui element to a python function which returns
# this ui element.

class UIElement2PyFuncCall(object):


    def __init__(self):
        return


    def render(self, element):
        self._imports = []
        self._funcnames = []
        self._funcs = []
        funcname = self._onElement(element)
        self._createVisualFunc(funcname)
        return self._generateTexts()


    def _createVisualFunc(self, funcname):
        f = _func()
        f.name = 'visual'
        f.args = ['director']
        f.body = ['return %s()' % funcname]
        self._funcs.append(f)
        return f


    def _generateTexts(self):
        text = []
        text.append( '# -*- Python -*-' )
        text.append( '# auto-generated by UIElement2PyFuncCall' )
        text.append( '' )

        text += self._imports
        text.append( '' )
        
        for func in self._funcs:
            text.append('def %s(%s):' % (
                func.name, (func.args or '') and ','.join(func.args)
                ) )
            for line in func.body:
                text.append('  '+line)
            text.append('')
            continue

        
        return text
    

    def _addImport(self, kls):
        m = kls.__module__
        name = kls.__name__
        statement = 'from %s import %s' % (m, name)
        if statement not in self._imports:
            self._imports.append(statement)
        return


    def _createElementName(self, element):
        theid = element.id
        if not theid: theid = id(element)
        
        typename = element.__class__.__name__.lower()
        candidate = typename + str(theid)
        candidate = nonalphanumeric.sub('_', candidate)
        
        if candidate in self._funcnames:
            raise RuntimeError, \
                  "unable to generate unqiue function name for element %s" % element
        
        return candidate
            

    def _onElement(self, element):
        kls = element.__class__
        self._addImport(kls)
        
        myfunc = _func()
        myfunc.name = self._createElementName(element)
        myfunc.body = []

        # code to create an instance
        myfunc.body.append('instance = %s()' % kls.__name__)

        # loop over descriptors
        descriptors = element.iterDescriptors()
        for descriptor in descriptors:
            type = descriptor.type
            name = descriptor.name
            value = descriptor.__get__(element)
            if type == 'referenceset':
                thelist = []
                for item in value:
                    if not isinstance(item, basestring):
                        if not item:
                            debug.log('None item encountered: descriptor %s(%s)' % (type, name))
                            continue
                        funcname = self._onElement(item)
                        thelist.append('%s()' % funcname)
                    else:
                        thelist.append(item)
                myfunc.body.append( 'instance.%s = [%s]' % (
                    name, ', '.join(thelist)) )
                    
            elif type == 'reference':
                if not value:
                    debug.log('None value encountered: descriptor %s(%s)' % (type, name))
                    continue
                funcname = self._onElement(value)
                myfunc.body.append( 'instance.%s = %s()' % (name,funcname) )
                
            else:
                if name == 'id' and not value: continue
                myfunc.body.append( 'instance.%s = %r' % (name, value) )
                
            continue

        # return statement
        myfunc.body.append('return instance')
        
        self._funcs.append(myfunc)
        
        return myfunc.name


import re
nonalphanumeric = re.compile('\W')


class _func:

    name = None
    args = None
    body = None



def test():
    from luban.content.Frame import Frame
    frame = Frame(name='mainframe', title='test')
    doc = frame.document(id='frame', title='test')
    renderer = UIElement2PyFuncCall()
    print '\n'.join(renderer.render(frame))

    return


def main():
    test()
    return


if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# End of file 
