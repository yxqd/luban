# -*- python -*-
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


class Loader:

    "extension loader"

    #
    loaded = []
    
    #
    def load1(self, ext):
        """load a luban extension

        Be careful with the sequence of loading extensions.
        Extension loaded later coule override the earlier one
        if extension_allow_override is True.
        """
        loaded_exts = self.loaded
        if ext in loaded_exts:
            return
        self._load1(ext)
        loaded_exts.append(ext)
        return


    def load(self, extensions):
        """load a list of extensions

        Be careful with the sequence of loading extensions.
        Extension loaded later coule override the earlier one
        if extension_allow_override is True.
        """
        for ext in extensions:
            self.load1(ext)
            continue
        return


    def _load1(self, ext):
        from .weaver.web.libraries.default import bundle as lib_bundle
        from .weaver.web.Library import Library

        module = '%s.luban_ext' % ext
        module = __import__(module, fromlist = [''])
        # 
        if hasattr(module, 'weaver_web_lib_extensions'):
            for name, exts in module.weaver_web_lib_extensions:
                try:
                    lib = Library.get(name)
                except KeyError:
                    lib = None
                if lib: # extend old lib
                    lib.extends(**exts)
                else: # create new lib
                    Library(name, **exts)
                continue
            pass

        #
        if hasattr(module, 'weaver_web_widgets_extensions'):
            for name, libs in module.weaver_web_widgets_extensions:
                setattr(lib_bundle, name, libs)
                continue
            pass

        # obsolete
        if hasattr(module, "jsfiles_toload_onstart"):
            import warnings
            warnings.warn("jsfiles_toload_onstart is obsolete. use weaver_web_lib_extensions")

        return

loader = Loader()


# End of file 

