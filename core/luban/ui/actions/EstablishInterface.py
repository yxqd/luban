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


from luban import py_major_ver
if py_major_ver == 2:
    from luban.ui import descriptors


from .Action import Action as base

class EstablishInterface(base):

    # decorations
    simple_description = 'establish a user interface'
    full_description = ('')

    
    # attributes
    frame = descriptors.element()
    

    def __init__(self, frame=None):
        '''establishInterface(frame) -> establish a UI from the frame
        '''
        if py_major_ver == 2:
            superme = super(EstablishInterface, self)
        elif py_major_ver == 3:
            superme = super()
            
        superme.__init__(frame=frame)
        return
    
    
    def identify(self, inspector):
        return inspector.onEstablishInterface(self)


# End of file 

