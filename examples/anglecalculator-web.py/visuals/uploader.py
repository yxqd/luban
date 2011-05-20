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
    doc = lc.document(title='Upload A Data File', id='uploader-doc')
    doc.Class = 'window'
    
    uploader = lc.uploader(
        name = 'uploaded',
        label='Upload data',
        onsubmit=lc.load(actor='main', routine='onpuload')
        )
    doc.add(uploader)
    return doc
    

# version
__id__ = "$Id$"

# End of file 
