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


# the main view factory. basically a dispatcher


from ObjectViewBase import Factory as base


class Factory(base):


    def __call__(self, obj=None, editor=True, **kwds):
        if editor:
            factory = self._createEditorViewFactory()
        else:
            factory = self._createReadOnlyViewFactory()
        if obj:
            return factory(obj, **kwds)
        else:
            return factory


    def _createEditorViewFactory(self):
        from EditorView import Factory
        return self._newFactory(Factory)
        
    
    def _createReadOnlyViewFactory(self):
        from ReadOnlyView import Factory
        return self._newFactory(Factory)
        
    
# version
__id__ = "$Id$"

# End of file 
