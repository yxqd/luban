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



class FormFieldActions(object):


    def showError(self, errorMessage):
        warnings.warn("element.showError is obsolete, please use element.formfield('showError', message=...)", DeprecationWarning)
        from SimpleElementAction import SimpleElementAction
        return SimpleElementAction(self, 'showerrormessage', message=errorMessage)


    def formfield(self, actionname, **kwds):
        if actionname == 'getSelectedLabel':
            warnings.warn('formselectorfield.formfield("getSelectedLabel") is obsolete, please us formselectorfield.getAttr("selection")', DeprecationWarning)
        from SimpleElementAction import SimpleElementAction
        return SimpleElementAction(self, actionname, **kwds)


import warnings


# version
__id__ = "$Id$"

# End of file 

