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
    doc = lc.document(id='mode-selector-doc')
    doc.Class = 'window'

    acc = lc.accordion(id='mode_selector'); doc.add(acc)

    bisecting = acc.section(label='Bisecting')
    scattering_plane = acc.section(label='Scattering plane')
    phi_fixed = acc.section(label='Phi fixed')

    from lattice_parameters import visual as lp
    bisecting.add(lp())

    from scattering_plane import visual as sp
    scattering_plane.add(lp())
    scattering_plane.add(sp())

    phi_fixed.add(lp())
    from fixed_phi import visual as fp
    phi_fixed.add(fp())
    
    return doc
    

# version
__id__ = "$Id$"

# End of file 
