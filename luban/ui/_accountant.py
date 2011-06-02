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


# registry of element providers
element_providers = ['luban.content']


def getElementClassesRecursivley(package=None, packages=None):
    if not packages:
        packages = [package]
        
    ret = []
    for pkg in packages:
        ret += _getElementClassesRecursivley(pkg)
        continue

    return ret


def _getElementClassesRecursivley(package='luban.content'):

    ret = getElementClasses(package)
    
    import os
    packagename = package
    package = __import__(packagename, {}, {}, [''])
    packagepath = os.path.dirname(package.__file__)
    for entry in os.listdir(packagepath):
        p = os.path.join(packagepath, entry)
        if os.path.isdir(p):
            subpkg = '.'.join([packagename, entry])
            ret += getElementClassesRecursivley(subpkg)
        continue
    return ret


def getElementClasses(package='luban.content'):
    # return a list of all UI element classes for luban in the given package
    
    import os
    packagename = package
    package = __import__(packagename, {}, {}, [''])
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
    def _importSymbols(package, name):
        path = package+'.'+name
        mod = __import__(path, {}, {}, [''])
        return mod.__dict__

    # classes
    symboldicts = map(lambda name: _importSymbols(packagename, name), modules)
    candidates = []
    for symboldict in symboldicts:
        for v in symboldict.itervalues():
            if v not in candidates: candidates.append(v)

    def _filter(candidate):
        isattributecontainer = candidate is not None \
            and isDerivedFromAttributeContainer(candidate)
        if not isattributecontainer: return False
        if hasattr(candidate, 'abstract'): return not candidate.abstract
        return True
    return filter(_filter, candidates)


def isDerivedFromAttributeContainer(klass):
    from luban.content.AttributeContainer import AttributeContainer
    if klass is AttributeContainer: return False
    try:
        return issubclass(klass, AttributeContainer)
    except:
        return False


# version
__id__ = "$Id$"

# End of file 
