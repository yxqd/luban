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


def stateHandler(m):
    """use this decorator on a routine that handles actions related
    to application "state"

    "m" must return a "frame" instance
    
    this decorator change the routine to either return
    a replacement action that replace current frame with the new frame
    or a frame establishment action,
    or the frame itself.
    """
    
    import luban
    def _(self, *args, **kwds):
        # returntype
        if 'returntype' not in kwds:
            kwds['returntype'] = 'establishinterface'
        rtype = kwds['returntype']
        # clear it from kwd args
        del kwds['returntype']

        # call the method to wrap
        frame = m(self, *args, **kwds)
        
        # depend on return type, return appropriate action
        if rtype == 'replaceframe':
            return luban.a.select(id='').replaceBy(newelement=frame)
        
        elif rtype == 'establishinterface':
            return luban.a.establishInterface(frame)
        
        return frame
    
    return _


# End of file 
