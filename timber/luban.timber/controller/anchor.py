# -*- Python -*-
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


def anchorHandler(m):
    """use this decorator on a routine that handles "setanchor" action

    such routine must return a "frame" instance

    this decorator change the routine to either return
    """
    import luban
    def _(self, *args, **kwds):
        frame = m(self, *args, **kwds)
        if 'returntype' not in kwds:
            kwds['returntype'] = 'establishinterface'

        rtype = kwds['returntype']
        if rtype == 'replaceframe':
            return luban.a.select(id='').replaceBy(newelement=frame)
        elif rtype == 'establishinterface':
            return luban.a.establishInterface(frame)
        return frame
    
    return _


# End of file 
