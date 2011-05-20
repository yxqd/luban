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


def typename2typeMap():
    klasses = getElementClasses()
    ret = {}
    for kls in klasses:
        ret[kls.__name__.lower()] = kls
    return ret


def getElementClasses():
    # return a list of all UI element classes for luban
    
    import luban.content as package
    import os
    packagepath = os.path.dirname(package.__file__)

    # names of the modules
    modules = []
    for entry in os.listdir(packagepath):
        name, ext = os.path.splitext(entry)
        
        # not python. omit
        if ext not in ['.py', '.pyc', '.pyo']: continue

        # duplidated. omit
        if name in modules: continue
        
        modules.append(name)
        continue

    #
    def _importElementClass(package, name):
        path = package+'.'+name
        mod = __import__(path, {}, {}, [''])
        try: return getattr(mod, name)
        except: return

    # classes
    packagename = 'luban.content'
    klasses = map(lambda name: _importElementClass(packagename, name), modules)
    klasses = filter(
        lambda klass: klass is not None,
        klasses)
    klasses = filter(
        lambda klass: isAttributeContainer(klass),
        klasses)

    return klasses


def isAttributeContainer(klass):
    from luban.content.AttributeContainer import AttributeContainer
    try:
        return issubclass(klass, AttributeContainer)
    except:
        return False


# version
__id__ = "$Id$"

# End of file 
