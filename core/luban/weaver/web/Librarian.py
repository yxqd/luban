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
manage mapping from {feature} to a library or libraries

a library is an instance of .Library.Library

{feature} could be 
* base: luban base
* application: luban application
* {widget}

css files are grouped under a css directory: cssbase,
and javascripts files under a js directory: jsbase

cssbase and jsbase are base directories of css and js
in the file system.

a library does not need to know this base.

A library looks like
 jquery:
   css: jquery.css
   javascript: jquery-1.x.y.js

In the filesystem, it would be sth like
 static/
   css/
     jquery.css
   javascripts/
     jquery-1.x.y.js

"""


class Librarian:

    reserved = ['base', 'application']

    def __init__(self, cssbase='css', jsbase='javascripts'):
        self.cssbase = cssbase
        self.jsbase = jsbase
        self._registry = {}
        #
        for r in self.reserved: self.register(r)
        return


    def register(self, feature, libraries=None):
        """register a feature with a library

        register("base", 'lib')
        register("accordion", 'luban.accordion')
        register("application", ['mylib1', 'mylib2'])
        """
        libraries = libraries or []
        try: iter(libraries)
        except TypeError:
            raise ValueError("%r is not iterable" % libraries)
            
        self._registry[feature] = libraries
        return


    def iterWidgets(self):
        reserved = self.reserved
        for k in self._registry.keys():
            if k in reserved: continue
            yield k
        return


    def iterLibraries(self, feature, exclude_libs = None):
        """iterate over libraries for the given feature

        exclude_libs: it is useful to skip over some libraries,
          since they could already loaded by the browser and
          don't need to be loaded again.
        """
        from .Library import extractAllDeps, Library
        libs = self._registry.get(feature)
        deps = extractAllDeps(libs, exclude_libs)
        for dep in deps: yield dep

        libs = map(Library.get, libs)
        for lib in libs: yield lib
        return


    def iterStyleSheets(self, feature=None, exclude_libs=None):
        """retrieve a list of style sheets needed
        by this feature
        """
        libraries = self.iterLibraries(feature, exclude_libs=exclude_libs)
        for lib in libraries:
            for css in lib.css:
                yield self._csspath(css)
            continue
        return


    def iterJavaScriptLibs(self, feature=None, exclude_libs=None):
        """retrieve a list of javascripts needed
        by this feature
        """
        libraries = self.iterLibraries(feature, exclude_libs=exclude_libs)
        for lib in libraries:
            for js in lib.javascripts:
                yield self._jspath(js)
            continue
        return 


    def _csspath(self, stylesheet):
        path = [self.cssbase, stylesheet]
        return '/'.join(path)
        
        
    def _jspath(self, jslib):
        path = [self.jsbase, jslib]
        return '/'.join(path)


# End of file 
