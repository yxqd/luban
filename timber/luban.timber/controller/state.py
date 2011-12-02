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
    from .decorators import frameHandler
    return frameHandler(m)


# End of file 
