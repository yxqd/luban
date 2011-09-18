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


# override aokuang.DemoPanelActor.createCodeDoc
def createCodeDoc(blocks):
    lines = []
    for block in blocks:
        if not block: continue
        lines += [l.rstrip() for i, l in block]
        continue
    
    import luban
    viewer = luban.e.codeviewer()
    viewer.syntax = 'python'
    viewer.text = '\n'.join(lines)
    return viewer
from aokuang import DemoPanelActor
DemoPanelActor.createCodeDoc = createCodeDoc


# End of file 
