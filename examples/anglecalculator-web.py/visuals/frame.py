# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import luban.content as lc
from luban.content import select, alert, load


def visual():
    frame = lc.frame(title='Calculator for Four Circle Neutron Diffractometers')

    grid = lc.grid(); frame.add(grid)
    
    upperdoc = lc.document(title='Known data', id='known-data-doc'); grid.row().cell().add(upperdoc)
    upperdoc.Class = 'window'
    
    splitter = upperdoc.splitter()
    upperleft = splitter.section(id='upperleft')
    upperright = splitter.section(id='upperright')

    from uploader import visual
    upperleft.add(visual())
    
    from observations import visual
    upperleft.add(visual())
    
    from mode_selector import visual
    upperright.add(visual())
    
    lowersp = lc.splitter(); grid.row().cell().add(lowersp)
    lowerleft = lowersp.section(id='lowerleft')
    lowerright = lowersp.section(id='lowerright')
    
    from ubmatrix import visual
    lowerleft.add(visual())
    
    from desired_results import visual
    lowerright.add(visual())
    return frame
    

# version
__id__ = "$Id$"

# End of file 
