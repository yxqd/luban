#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                        California Institute of Technology
#                        (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


saved_warnings_showwarning = None
called = False

def redirectWarningsToJournal(channel):
    '''channel: debug/warning/error
    '''
    if called: return
    import journal
    factory = getattr(journal, channel)

    # overload warnings.showwarning
    import warnings
    global saved_warnings_showwarning
    if saved_warnings_showwarning is None:
        saved_warnings_showwarning = warnings.showwarning

    def showwarning(message, category, filename, lineno, file=None, line=None):
        m = '%s:%s: %s: %s' % (filename, lineno, category.__name__, message)
        factory(category.__name__).log(m)
        return
    warnings.showwarning = showwarning
    return


def ignoreWarnings():
    import warnings
    def showwarning(message, category, filename, lineno, file=None, line=None):
        return
    warnings.showwarning = showwarning
    return


# version
__id__ = "$Id$"

# End of file 
