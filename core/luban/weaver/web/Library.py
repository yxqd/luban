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


"""
a library associates a name with a bunch of css and javascript
modules.
"""

class Library:

    registry = {}

    @classmethod
    def get(cls, name):
        return cls.registry[name]


    @classmethod
    def reset(cls):
        cls.registry = {}
        return
    
    
    def __init__(
        self, name,
        css=None, javascripts=None, dependencies=None,
        website = None,
        replace=False):
        
        if name in self.registry and not replace:
            old = self.get(name)
            raise RuntimeError("attempt to register library %r(css=%r, javascripts=%r, deps=%r) failed. already registered as %s." % (
                name, css, javascripts, dependencies, old))

        if isinstance(css, str):
            raise ValueError("css should be a list")
        if isinstance(javascripts, str):
            raise ValueError("javascripts should be a list")
        if isinstance(dependencies, str):
            raise ValueError("dependenciess should be a list")

        self.registry[name] = self
        
        self.name = name
        self.css = css or []
        self.javascripts = javascripts or []
        self.dependencies = dependencies or []
        self.website = website
        return


    def extends(self, css=None, javascripts=None, dependencies=None):
        "extend this library to add new stylesheets, javascript modules, or dependencies"
        if css: self.css += css
        if javascripts: self.javascripts += javascripts
        if dependencies: self.dependencies += dependencies
        return
    
    
    def __repr__(self):
        return 'Library(%r, css=%r, javascripts=%r, dependencies=%r)' % (
            self.name, self.css, self.javascripts, self.dependencies)
    
    
    def extractAllCss(self, exclude_libs=None):
        deps = self.extractAllDeps(exclude_libs = exclude_libs)
        for dep in deps:
            for t in dep.css: yield t
            continue
        for t in self.css: yield t
        return        
    

    def extractAllJavascripts(self, exclude_libs=None):
        deps = self.extractAllDeps(exclude_libs = exclude_libs)
        for dep in deps:
            for t in dep.javascripts: yield t
            continue
        for t in self.javascripts: yield t
        return        
    

    def extractAllDeps(self, exclude_libs=None):
        """extract all dependent libraries of this library
        """
        return iter(extractAllDeps(self.dependencies, exclude_libs))


def extractAllDeps(libs, exclude_libs=None):
    """extract all dependent libraries of the given sequence of libraries
    """
    exclude_libs = exclude_libs or []
    exclude_libs = map(Library.get, exclude_libs)

    # expand exclude_libs so that the list include
    # all dependencies of the excluded libraries.
    # the reason of doing that is we assume the excluded
    # libraries and their dependencies are already in place
    # and no longer need to be take into account
    exclude_libs = list(expandAll(exclude_libs))

    #
    try: iter(libs)
    except TypeError:
        raise ValueError("%s is not iterable" % libs)
    
    deps = map(Library.get, libs)
    for dep in deps:
        if dep in exclude_libs: continue

        for t in dep.extractAllDeps():
            if t in exclude_libs: continue
            yield t
            # t should be excluded now since it is already
            # in the "include" list
            exclude_libs.append(t)
            continue

        yield dep
        # dep should be excluded now since it is already
        # in the "include" list
        exclude_libs.append(dep)
        continue
    return


def expandAll(libs):
    """expand libs (an iterator) to include all libs and their dependecies 
    """
    yielded = []
    for lib in iter(libs):
        if lib in yielded: continue
        for t in lib.extractAllDeps():
            if t in yielded: continue
            yield t
            yielded.append(t)
            continue
        yield lib
        yielded.append(lib)
        continue
    return
            

def expand(lib):
    """expand a lib to include all of its dependecies and itself
    """
    yielded = []
    for dep in lib.extractAllDeps():
        yield dep
        continue
    yield lib
    return
            

# End of file 
